---
title: A Zeroth-Order Paradigm for LLM Preference Alignment
title_zh: 零阶范式下的LLM偏好对齐方法ComPO
authors:
- Peter Chen
- Xi Chen
- Wotao Yin
- Tianyi Lin
affiliations:
- UC Berkeley
- New York University
- Alibaba DAMO Academy
- Columbia University
arxiv_id: '2609.19144'
url: https://arxiv.org/abs/2609.19144
pdf_url: https://arxiv.org/pdf/2609.19144
published: '2026-09-15'
collected: '2026-09-17'
category: Training
direction: LLM偏好对齐 · 零阶优化方法
tags:
- Preference Alignment
- Zeroth-Order Optimization
- DPO
- LLM Training
- KL Regularization
one_liner: 提出基于比较Oracle的零阶偏好对齐方法，利用低置信度偏好对提升对齐效果并缓解似然偏移
practical_value: '- 垂域LLM/电商Agent对齐时，无需直接丢弃低似然差的噪声偏好对，可复用ComPO的比较Oracle思路，仅用这类对判断参数微扰的优化方向，不直接计算损失，既利用数据价值又规避似然偏移问题

  - 资源受限的对齐场景可借鉴仅微调输出层+稀疏梯度裁剪的方案，ComPO更新参数仅占7B模型的0.02%，单卡显存峰值比DPO低60%以上，无需高端GPU即可完成对齐调优

  - 生成式推荐/多轮对话Agent对齐时，可复用在线ComPO的反向KL软阻尼+有效batch回放机制，用当前模型无标注生成控制更新步长，避免对齐后输出偏离用户真实分布，提升多轮交互稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有DPO类直接偏好对齐方法处理低似然差的噪声偏好对时，易出现似然偏移问题：仅优化偏好与非偏好响应的相对似然差，可能导致偏好响应的绝对概率下降，甚至将概率质量迁移到有害响应；直接过滤这类对又会浪费其中蕴含的有效比较信息，亟需兼顾数据利用与稳定性的对齐方案。

### 方法关键点
- 提出零阶对齐方法ComPO，基于比较Oracle做参数微扰，仅通过「偏好响应似然上升、非偏好响应似然下降」的二元判断得到更新方向，无需直接对偏好对计算可微损失
- 离线流程：将偏好对按参考模型似然差拆分为干净/噪声子集，先在干净子集上运行DPO/SimPO做基础对齐，再用ComPO在噪声子集上仅微调输出层，配合梯度稀疏裁剪过滤小幅度无效更新
- 在线扩展：保留离线比较逻辑，用当前模型无标注生成计算长度归一化的反向KL代理指标做步长软阻尼，加入有效更新mini-batch回放机制进一步提升稳定性

### 关键结果
基于UltraFeedback数据集，在Mistral、Llama、Gemma、Qwen等5类模型上测试，对比DPO、SimPO基线：
- 离线DPO+ComPO在AlpacaEval 2长度控制胜率上平均提升2~3pct，Mistral-7B-Instruct的MT-Bench得分从5.86提升至7.69
- 在线ComPO加入阻尼+回放后，Gemma-3-4B-it的Arena-Hard胜率比离线版高6pct
- 7B模型上ComPO仅更新0.02%参数，单卡显存峰值16.3GB，比DPO低70%左右

> 最值得记住的结论：低置信度偏好对不是无效数据，用比较式零阶优化处理可以同时实现效果提升与似然偏移缓解
