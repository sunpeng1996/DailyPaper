---
title: 'LESSER: Post-Training Data Selection with Output-Layer Gradients'
title_zh: LESSER：基于输出层梯度的大模型后训练数据选择方法
authors:
- Lyuxin David Zhang
- Eric Wong
- Surbhi Goel
- Anton Xue
affiliations:
- University of Pennsylvania
- University of Texas at Austin
arxiv_id: '2610.03702'
url: https://arxiv.org/abs/2610.03702
pdf_url: https://arxiv.org/pdf/2610.03702
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 大模型训练 · 高效数据选择
tags:
- DataSelection
- PostTraining
- Efficiency
- SFT
- RL
- Gradient
one_liner: 用输出层梯度替代全参数梯度做后训练数据选择，成本骤降同时性能接近全梯度方法
practical_value: '- 做垂直领域LLM SFT/RLHF（比如电商商品文案生成、query理解、推荐Agent决策微调）时，可直接用LESSER替代全梯度数据选择方法，特征提取成本降9.7×（SFT）/3×（RL），下游性能仅差1.3个点，大幅降低数据筛选开销

  - 工程实现简单，仅需前向传播获取最后一层隐状态、输出概率即可计算选择特征，无需修改原有数据选择管道逻辑，可作为drop-in组件直接替换

  - 当数据筛选成本超过训练本身成本时，优先选择输出层梯度类轻量化特征，不需要追求单样本梯度和全梯度的完全对齐，批量梯度对齐即可保障下游效果

  - 可复用该思路优化推荐场景的样本筛选：做召回/排序模型训练的高价值样本筛选时，用输出层梯度替代全梯度做样本选择，降低计算开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
基于全参数梯度的LLM后训练数据选择需对每个候选样本执行反向传播，大候选池下计算成本极高，甚至超过训练选中样本的开销，亟需低成本的梯度近似方案同时保障选择效果。
### 方法关键点
- 仅用输出层梯度替代全参数梯度作为数据选择特征，无需修改原有数据选择规则，可作为drop-in组件直接适配LESS、GradAlign、GRACE等现有梯度类选择方法
- 输出层梯度可直接通过前向传播得到的最后一层隐状态、输出概率计算，完全不需要反向传播，计算成本大幅降低
- 支持低维投影进一步压缩特征，降低存储和相似性计算开销
### 关键实验
SFT场景下以19.7万条Tulu V2指令为候选池，覆盖5类下游任务，对比LESS、RDS+、Random基线，特征提取FLOP降低9.7×、wall-clock降低17.8×，下游性能和LESS平均仅差1.3个点；RL场景下，相比全梯度GradAlign FLOP降低3×、单轮得分时间降低3.5×，最终测试准确率完全对齐；蒸馏教师选择场景下，特征提取时间降低3.9~5.4×，选出的最优教师和全梯度方法完全一致。
### 核心结论
高效数据选择特征不需要追求单样本与全梯度的完全对齐，只要保障批量梯度的方向对齐即可，输出层梯度是兼顾效果和成本的极佳选择。
