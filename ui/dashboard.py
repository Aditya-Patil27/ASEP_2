import cv2
import numpy as np
from typing import Dict, Any
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Dashboard:
    def __init__(self):
        """
        Initialize dashboard
        """
        self.root = tk.Tk()
        self.root.title("Autonomous Car Dashboard")
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create video display
        self.video_label = ttk.Label(self.main_frame)
        self.video_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        # Create status indicators
        self.create_status_frame()
        
        # Create sensor data plot
        self.create_sensor_plot()
        
        # Create control buttons
        self.create_control_buttons()
        
        # Initialize data storage
        self.sensor_data = {
            'speed': [],
            'battery': [],
            'distance': []
        }
        
    def create_status_frame(self):
        """
        Create status indicators frame
        """
        status_frame = ttk.LabelFrame(self.main_frame, text="Status", padding="5")
        status_frame.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Status labels
        self.status_labels = {}
        status_items = [
            ('Mode', 'Autonomous'),
            ('Speed', '0.0 m/s'),
            ('Battery', '100%'),
            ('Distance', '0.0 m')
        ]
        
        for i, (label, value) in enumerate(status_items):
            ttk.Label(status_frame, text=f"{label}:").grid(row=i, column=0, sticky=tk.W)
            self.status_labels[label] = ttk.Label(status_frame, text=value)
            self.status_labels[label].grid(row=i, column=1, sticky=tk.W)
            
    def create_sensor_plot(self):
        """
        Create sensor data plot
        """
        plot_frame = ttk.LabelFrame(self.main_frame, text="Sensor Data", padding="5")
        plot_frame.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Create matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(4, 3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=(tk.W, tk.E))
        
    def create_control_buttons(self):
        """
        Create control buttons
        """
        control_frame = ttk.Frame(self.main_frame)
        control_frame.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Control buttons
        ttk.Button(control_frame, text="Start", command=self.start).grid(row=0, column=0, padx=5)
        ttk.Button(control_frame, text="Stop", command=self.stop).grid(row=0, column=1, padx=5)
        ttk.Button(control_frame, text="Reset", command=self.reset).grid(row=0, column=2, padx=5)
        
    def update_video(self, frame: np.ndarray):
        """
        Update video display
        Args:
            frame: Input frame
        """
        # Convert frame to PhotoImage
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (640, 480))
        image = tk.PhotoImage(data=cv2.imencode('.ppm', frame)[1].tobytes())
        self.video_label.configure(image=image)
        self.video_label.image = image
        
    def update_status(self, status: Dict[str, Any]):
        """
        Update status indicators
        Args:
            status: Status dictionary
        """
        for key, value in status.items():
            if key in self.status_labels:
                self.status_labels[key].configure(text=str(value))
                
    def update_sensor_data(self, data: Dict[str, float]):
        """
        Update sensor data plot
        Args:
            data: Sensor data dictionary
        """
        # Update data storage
        for key, value in data.items():
            if key in self.sensor_data:
                self.sensor_data[key].append(value)
                if len(self.sensor_data[key]) > 100:  # Keep last 100 points
                    self.sensor_data[key].pop(0)
                    
        # Update plot
        self.ax.clear()
        for key, values in self.sensor_data.items():
            self.ax.plot(values, label=key)
            
        self.ax.set_title("Sensor Data")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Value")
        self.ax.legend()
        self.ax.grid(True)
        
        self.canvas.draw()
        
    def start(self):
        """
        Start autonomous operation
        """
        self.status_labels['Mode'].configure(text="Autonomous")
        
    def stop(self):
        """
        Stop autonomous operation
        """
        self.status_labels['Mode'].configure(text="Manual")
        
    def reset(self):
        """
        Reset dashboard
        """
        # Clear sensor data
        for key in self.sensor_data:
            self.sensor_data[key] = []
            
        # Reset status
        self.update_status({
            'Mode': 'Manual',
            'Speed': '0.0 m/s',
            'Battery': '100%',
            'Distance': '0.0 m'
        })
        
        # Update plot
        self.update_sensor_data({})
        
    def run(self):
        """
        Start dashboard main loop
        """
        self.root.mainloop()
        
    def __del__(self):
        """
        Clean up resources
        """
        if hasattr(self, 'root'):
            self.root.destroy() 