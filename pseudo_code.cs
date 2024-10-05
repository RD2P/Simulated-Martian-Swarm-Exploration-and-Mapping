using System;
using System.Collections.Generic;
using System.Numerics; // For Vector3

public class Swarm {
    private List<Drone> drones;
    public Vector3 TargetCoordinate { get; private set; }

    public Swarm() {
        drones = new List<Drone>();
    }

    // Add drones to the swarm
    public void AddDrone(Drone drone) {
        drones.Add(drone);
        drone.AssignSwarm(this); // Provide reference to the swarm instance
    }

    // Set the shared target coordinate for the entire swarm
    public void SetTarget(Vector3 target) {
        TargetCoordinate = target;
        Console.WriteLine($"Swarm target set to: {target}");
    }

    // Method to start the swarm's movement (initiates all drones)
    public void StartExploring() {
        foreach (Drone drone in drones) {
            drone.Start();
        }
    }
}


public class Drone {
    private Swarm swarm; // Reference to the shared Swarm instance
    private Vector3 position;
    private float speed = 1.0f; // Speed of the drone

    public Drone() {
        position = Vector3.Zero; // Starting position
    }

    // Assign the shared swarm instance
    public void AssignSwarm(Swarm swarmInstance) {
        swarm = swarmInstance;
    }

    // Start the drone's autonomous behavior
    public void Start() {
        while (true) {
            MoveTowardsSwarmTarget();
            AvoidCollision();
            TakePhoto();
            SendDataToRover();
        }
    }

    // Movement logic towards the swarm's target coordinate
    private void MoveTowardsSwarmTarget() {
        if (swarm == null) return; // Ensure the drone has a swarm reference

        // Get the target from the shared Swarm instance
        Vector3 target = swarm.TargetCoordinate;

        // Calculate direction towards the target
        Vector3 direction = Vector3.Normalize(target - position);
        
        // Update position towards the target
        position += direction * speed;
        
        // Check if target is reached (or within a small threshold)
        if (Vector3.Distance(position, target) < 0.5f) {
            // Target reached; perform an action if necessary
        }
    }

    private void AvoidCollision() {
        // Simple collision avoidance logic
    }

    private void TakePhoto() {
        // Capture photo at the current position
    }

    private void SendDataToRover() {
        // Send photo data to the rover
    }
}


public class Rover {
    private Swarm swarm;

    public Rover() {
        swarm = new Swarm();
    }

    public void DeploySwarm(int numberOfDrones) {
        for (int i = 0; i < numberOfDrones; i++) {
            Drone drone = new Drone();
            swarm.AddDrone(drone);
        }

        // Set a target for the swarm and start exploration
        Vector3 targetCoordinate = new Vector3(10, 0, 10);
        swarm.SetTarget(targetCoordinate);
        swarm.StartExploring();
    }
}