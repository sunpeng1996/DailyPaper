---
title: Sample-Efficient Learning from Agent Experience
title_zh: 智能体交互经验的样本高效蒸馏学习方法
authors:
- Chenhui Gou
- Haoqin Tu
- Yunhao Fang
- Jianfei Cai
- Hamid Rezatofighi
affiliations:
- Monash University
- ByteDance Seed
arxiv_id: '2607.21051'
url: https://arxiv.org/abs/2607.21051
pdf_url: https://arxiv.org/pdf/2607.21051
published: '2026-07-22'
collected: '2026-07-24'
category: Agent
direction: 智能体训练 · 经验蒸馏
tags:
- Agent Training
- Experience Distillation
- In-Context Learning
- Context Distillation
- Sample Efficiency
one_liner: 提出无需额外环境交互的经验蒸馏方法，将智能体ICL收益固化到权重，样本效率远超RL基线
practical_value: '- 电商导购/客服Agent训练可复用1-step分支蒸馏思路，将历史交互经验固化到模型权重，无需额外真实用户交互，大幅降低训练成本

  - 微调大模型时可复用Branch Packing trick，将多轮交互样本打包为单条训练序列，训练步骤减少90%以上，几乎不损失性能

  - 生成式推荐/搜索Agent迭代可采用「ICL试错+经验蒸馏」范式替代传统RL，用至少9倍更少的环境样本达到同等效果，适合流量成本高的业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
真实场景下智能体与环境交互成本极高（如电商用户反馈、软件任务测试、真实实验均需大量时间人力），传统RL样本效率极低难以落地；In-context learning（ICL）虽能利用交互历史快速提升性能，但收益不固化，移除上下文即消失；现有上下文蒸馏方法需要额外环境交互或世界模型，易引入误差、提升成本，因此亟需无需额外交互的经验蒸馏方案，将ICL收益固化到模型权重。

### 方法关键点
- 1-step分支蒸馏目标：仅基于已收集的历史交互轨迹的每个决策点，让带经验上下文的教师模型生成最优决策，学生模型不带上下文拟合该决策，无需世界模型或额外环境交互
- 经验预处理：对原始交互历史摘要降噪，浓缩关键反馈信息，适配教师上下文窗口，提升信息密度
- 增强教师推理：给教师加入固定推理prompt，引导其基于经验充分思考后生成决策，提升蒸馏后性能
- 分支打包：将同一轨迹的多组<历史前缀+教师决策>样本打包为单条训练序列，仅对教师生成的决策计算损失，大幅降低训练和推理成本

### 关键结果
在749个软件工程任务、6个文本冒险游戏上测试，对比ICL、SFT、PPO/GRPO等基线：
- 经验蒸馏保留至少64.8%的ICL收益，直接SFT仅保留3.8%
- ICL+经验蒸馏组合比传统RL基线少用至少9.6倍环境样本，性能更高
- 分支打包将总训练时间降低10倍以上，平均ICL收益保留率从84.2%提升到90.1%
- 蒸馏能力可跨任务泛化，OOD软件工程任务pass@1从4.62%提升到8.84%

最值得记住的结论：对于交互成本高的智能体场景，少量试错ICL+经验蒸馏是比传统RL性价比高得多的训练范式。
