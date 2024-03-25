import matplotlib.pyplot as plt

minimax_data = {
    "Board": ["b3", "b4"],
    "# Boards": [549946, 8146001],
    "Time": [21.290376901626587, 306.3955090045929]
}

minimax_alpha_beta_data = {
    "Board": ["b3", "b4"],
    "# Boards": [18297, 32201],
    "Time": [0.7763669490814209, 1.3025169372558594]
}

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('MiniMax vs MiniMax w/ Alpha Beta')

axs[0, 0].bar(minimax_data["Board"], minimax_data["Time"], color='blue')
axs[0, 0].set_title('MiniMax - Time')
axs[0, 0].set_ylabel('Time (seconds)')

axs[0, 1].bar(minimax_alpha_beta_data["Board"], minimax_alpha_beta_data["Time"], color='orange')
axs[0, 1].set_title('MiniMax w/ Alpha Beta - Time')
axs[0, 1].set_ylabel('Time (seconds)')

axs[1, 0].bar(minimax_data["Board"], minimax_data["# Boards"], color='blue')
axs[1, 0].set_title('MiniMax - # Boards')
axs[1, 0].set_ylabel('Number of Boards Explored')

axs[1, 1].bar(minimax_alpha_beta_data["Board"], minimax_alpha_beta_data["# Boards"], color='orange')
axs[1, 1].set_title('MiniMax w/ Alpha Beta - # Boards')
axs[1, 1].set_ylabel('Number of Boards Explored')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

