---
title: 'Predictable GRPO: A Closed-Form Model of Training Dynamics'
title_zh: 可预测GRPO：训练动力学的闭式解析模型
authors:
- Rajat Ghosh
- Datta Nimmaturi
- Aryan Singhal
- Vaishnavi Bhargava
- Henry Wong
- Johnu George
- Debojyoti Dutta
affiliations:
- Nutanix
- Unsloth
arxiv_id: '2606.30789'
url: https://arxiv.org/abs/2606.30789
pdf_url: https://arxiv.org/pdf/2606.30789
published: '2026-06-29'
collected: '2026-07-01'
category: Training
direction: 大模型RL后训练 · GRPO动力学建模
tags:
- GRPO
- RLHF
- TrainingDynamics
- HyperparameterTuning
- LLMAlignment
one_liner: 将GRPO训练简化为闭式阻尼振子模型，可预测训练轨迹、稳定性阈值和组大小不变性
practical_value: '- 调参优化：复用论文给出的GRPO稳定性阈值公式 `KηKref < 1−µ` 作为超参数校验规则，避免盲目试错，大幅降低RL对齐训练的不稳定概率

  - 算力节省：GRPO的组大小G仅影响训练噪声不影响均值收敛轨迹，可根据算力预算和噪声容忍度灵活选择G，无需盲目追求大G提升最终效果，最高可减少75%的采样成本

  - 故障诊断：直接复用论文提出的4类GRPO训练失效诊断指标（训练-评估耦合度、优势退化度、策略集中度、动力学稳定性），可快速定位训练失效原因，无需仅靠reward曲线盲目排查

  - 效率提升：做Agent对齐、生成式推荐RL调优时，可用论文的闭式三阶段轨迹公式拟合早期训练数据，提前预测收敛时间和最终reward天花板，提前终止无效训练'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
GRPO已成为LLM RL后训练提升推理能力的标准算法，但训练动力学完全依赖经验描述，超参数调优全靠试错，训练失败原因难以定位，前沿大模型RL训练算力成本极高，亟需可解释的动力学模型指导训练、降低成本。

### 方法关键点
- 基于平均场假设，将GRPO更新过程简化为带随机扰动的阻尼振子，有效质量、阻尼、刚度系数可通过优化器超参数和可测量的曲率直接闭式计算，无需拟合
- 证明过往经验性的单指数饱和reward曲线只是该模型的过阻尼极限，补充了单指数无法解释的慢启动阶段，可完整描述慢启动-快速上升-饱和三阶段训练轨迹
- 给出三个可证伪的量化预测：确定性轨迹与组大小G无关（仅波动幅度随1/G下降）、采样策略刷新间隔Kref存在尖锐的稳定性阈值、存在过阻尼到振荡的相变
- 提出4类可落地的故障诊断方法，可区分reward曲线无法分辨的奖励破解、优势退化、策略集中、动力学不稳定四类失效模式

### 关键结果
在GSM8K数据集上对3个不同规模的LLM做GRPO训练，闭式三阶段轨迹拟合训练reward的R²≥0.91；组大小从4提升到16时均值轨迹基本一致，仅波动幅度下降，与预测完全吻合；软最大化老虎机实验完美复现了过阻尼到振荡的相变和稳定性阈值。

### 核心结论
GRPO的训练轨迹本质上是由动量和离策略滞后提供惯性的二阶阻尼振荡过程，所有超参数的影响都可以通过振子的三个核心系数统一解释。
