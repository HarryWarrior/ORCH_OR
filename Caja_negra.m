%% === Código de la caja negra ============================================
% Simulación de la dinámica cuántica en MATLAB (caja negra)

clear; clc; close all;

% 1. Definir los estados iniciales
num_qubits = 3;                                            % Número de qubits
psi0 = kron([1;0], kron([1;0], [1;0]));                    % Estado inicial |000⟩

% 2. Definir las compuertas cuánticas
H    = (1/sqrt(2))*[1 1; 1 -1];                            % Compuerta Hadamard
X    = [0 1; 1 0];                                         % Compuerta X (NOT)
Y    = [0 -1i; 1i 0];                                      % Compuerta Y
Z    = [1 0; 0 -1];                                        % Compuerta Z
CNOT = [1 0 0 0; 0 1 0 0; 0 0 0 1; 0 0 1 0];                % Compuerta CNOT

% 3. Aplicar las compuertas al estado inicial
%    Superposición en q0 y q1
psi = kron(H, kron(H, eye(2))) * psi0;
%    Entrelazamiento entre q0 y q1
psi = kron(CNOT, eye(2)) * psi;
%    Entrelazamiento entre q1 y q2
psi = kron(eye(2), CNOT) * psi;

% 4. Simular decoherencia (ruido de fase y amplitud)
theta_phase = 0.1;                                         % Ángulo de ruido de fase
theta_amp   = 0.05;                                        % Ángulo de ruido de amplitud
Rz = [exp(-1i*theta_phase/2) 0; 0 exp(1i*theta_phase/2)];  % Ruido de fase
Rx = [cos(theta_amp/2) -1i*sin(theta_amp/2); ...
      -1i*sin(theta_amp/2)  cos(theta_amp/2)];             % Ruido de amplitud
%    Aplicar ruido a los qubits
psi = kron(Rz, kron(Rx, eye(2))) * psi;

% 5. Simular fluctuaciones ambientales (rotaciones aleatorias)
theta_x = 0.05;  theta_y = 0.03;  theta_z = 0.02;          % Pequeñas rotaciones
Rx_fluct = [cos(theta_x/2) -1i*sin(theta_x/2); ...
            -1i*sin(theta_x/2) cos(theta_x/2)];
Ry_fluct = [cos(theta_y/2) -sin(theta_y/2); ...
             sin(theta_y/2)  cos(theta_y/2)];
Rz_fluct = [exp(-1i*theta_z/2) 0; 0 exp(1i*theta_z/2)];
%    Aplicar fluctuaciones a los qubits
psi = kron(Rx_fluct, kron(Ry_fluct, Rz_fluct)) * psi;

% 6. Medición en la base Z
probabilities = abs(psi).^2;                               % Probabilidades
disp('Probabilidades de los estados (3 qubits):');
disp(probabilities.');

% 7. Simular mediciones
num_shots = 1000;                                          % Número de mediciones
measurements = randsample(1:2^num_qubits, num_shots, true, probabilities);
figure;
histogram(measurements, 'Normalization', 'probability');
xlabel('Estado'); ylabel('Probabilidad');
title('Histograma de mediciones (3 qubits)');

%% === Código de la caja gris =============================================
% Refinamiento del modelo con conocimiento adicional

% 8. Definir tasas de decoherencia para la caja gris
gamma_phase = 0.1;  gamma_amp = 0.05;                      % (gamma_amp no usado)

% 9. Evolución temporal simple de la coherencia
T  = 1;  dt = 0.01;  time = 0:dt:T;
coherence_simple = exp(-gamma_phase * time);               % Decaimiento simple

figure;
plot(time, coherence_simple, 'LineWidth', 2);
xlabel('Tiempo'); ylabel('Coherencia');
title('Evolución temporal de la coherencia (modelo simple)');
grid on;

%% 10. Hamiltoniano detallado (5 qubits) -----------------------------------
nq  = 5;
dim = 2^nq;
psi0_5  = zeros(dim,1);
psi0_5(1) = 1;
H_5 = kron(H, kron(H, kron(H, kron(eye(2), eye(2))))); % Hadamard en q0, q1, q2
psi0_5 = H_5 * psi0_5;
% Aplicar entrelazamiento similar al caso de 3 qubits
CNOT_5_01 = kron(CNOT, kron(eye(2), kron(eye(2), eye(2)))); % CNOT entre q0-q1
CNOT_5_12 = kron(eye(2), kron(CNOT, kron(eye(2), eye(2)))); % CNOT entre q1-q2
CNOT_5_23 = kron(eye(2), kron(eye(2), kron(CNOT, eye(2)))); % CNOT entre q2-q3
psi0_5 = CNOT_5_23 * CNOT_5_12 * CNOT_5_01 * psi0_5;
% 8. Definir el Hamiltoniano del sistema de microtubulos
% Energia de los estados individuales
epsilon = [0.1, 0.2, 0.15, 0.25, 0.3]; % Energias de los qubits
H_energy = epsilon(1) * kron(Z, kron(eye(2), kron(eye(2), kron(eye(2), eye(2))))) + ...
           epsilon(2) * kron(eye(2), kron(Z, kron(eye(2), kron(eye(2), eye(2))))) + ...
           epsilon(3) * kron(eye(2), kron(eye(2), kron(Z, kron(eye(2), eye(2))))) + ...
           epsilon(4) * kron(eye(2), kron(eye(2), kron(eye(2), kron(Z, eye(2))))) + ...
           epsilon(5) * kron(eye(2), kron(eye(2), kron(eye(2), kron(eye(2), Z))));

% Acoplamiento entre microtubulos
J = [0.05, 0.03, 0.02, 0.04, 0.01]; % Fuerzas de acoplamiento
H_coupling = J(1) * (kron(X, kron(X, kron(eye(2), kron(eye(2), eye(2))))) + ...
                     kron(Y, kron(Y, kron(eye(2), kron(eye(2), eye(2))))) + ...
                     kron(Z, kron(Z, kron(eye(2), kron(eye(2), eye(2)))))) + ...
             J(2) * (kron(eye(2), kron(X, kron(X, kron(eye(2), eye(2))))) + ...
                     kron(eye(2), kron(Y, kron(Y, kron(eye(2), eye(2))))) + ...
                     kron(eye(2), kron(Z, kron(Z, kron(eye(2), eye(2)))))) + ...
             J(3) * (kron(eye(2), kron(eye(2), kron(X, kron(X, eye(2))))) + ...
                     kron(eye(2), kron(eye(2), kron(Y, kron(Y, eye(2))))) + ...
                     kron(eye(2), kron(eye(2), kron(Z, kron(Z, eye(2)))))) + ...
             J(4) * (kron(eye(2), kron(eye(2), kron(eye(2), kron(X, X)))) + ...
                     kron(eye(2), kron(eye(2), kron(eye(2), kron(Y, Y)))) + ...
                     kron(eye(2), kron(eye(2), kron(eye(2), kron(Z, Z)))));

% Decoherencia (ruido de fase)
gamma = [0.01, 0.02, 0.015, 0.025, 0.03]; % Tasas de decoherencia
H_decoherence = gamma(1) * kron(Z, kron(eye(2), kron(eye(2), kron(eye(2), eye(2))))) + ...
                gamma(2) * kron(eye(2), kron(Z, kron(eye(2), kron(eye(2), eye(2))))) + ...
                gamma(3) * kron(eye(2), kron(eye(2), kron(Z, kron(eye(2), eye(2))))) + ...
                gamma(4) * kron(eye(2), kron(eye(2), kron(eye(2), kron(Z, eye(2))))) + ...
                gamma(5) * kron(eye(2), kron(eye(2), kron(eye(2), kron(eye(2), Z))));

% Hamiltoniano total
H_total = H_energy + H_coupling + H_decoherence;

% 9. Resolver la Ecuacion de Schrodinger dependiente del tiempo
T = 1; % Tiempo total
dt = 0.01; % Paso de tiempo
time = 0:dt:T;
psi_t = zeros(length(psi0_5), length(time)); % Estado en cada tiempo
psi_t(:, 1) = psi0_5; % Estado inicial

% Funcion para la Ecuacion de Schrodinger
schrodinger_eq = @(t, psi) -1i * H_total * psi; % -i * H * psi

% Resolver usando ode45 (solver de ecuaciones diferenciales)
[~, psi_t] = ode45(@(t, psi) schrodinger_eq(t, psi), time, psi0_5);

% 10. Graficar la evolucion de la coherencia
coherence = zeros(1, length(time));
for i = 1:length(time)
    coherence(i) = abs(psi_t(i, 1)); % Coherencia del primer qubit
end

figure;
plot(time, coherence, 'LineWidth', 2);
xlabel('Tiempo');
ylabel('Coherencia');
title('Evolucion temporal de la coherencia');
grid on;
%% Histograma de mediciones para 5 qubits
num_shots = 1000;                 % número de mediciones
psi_final_5 = psi_t(end, :).';    % Estado final del sistema de 5 qubits
prob5 = abs(psi_final_5).^2;      % probabilidades (32×1)                             
disp('Probabilidades de los estados (5 qubits):');
disp(prob5.');
% 1…32 en MATLAB corresponden a |00000⟩ … |11111⟩
num_qubits = 5;
measure5 = randsample(1:2^num_qubits, num_shots, true, prob5);
% Histograma normalizado
figure;
histogram(measure5 , 'Normalization','probability');

% Etiquetas de los ejes en binario de 5 bits
xticks(1:2:32);  % '00000', '00001', … '11111'
xlabel('Estado (binario)');
ylabel('Probabilidad');
title('Histograma de mediciones (5 qubits)');
grid on;