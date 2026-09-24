---
title: 'When and Where to Trust the Teacher: Unifying On-Policy Distillation and GRPO
  through Entropy-Calibrated Credit Assignment'
title_zh: 基于熵校准信用分配统一在线策略蒸馏与GRPO的训练方法
authors:
- Jie Zhang
- Jingxiao Yang
- Zhehao Huang
- Yuhang Liu
- Xiaolin Huang
affiliations:
- Shanghai Jiao Tong University
- Zhejiang University
arxiv_id: '2609.28385'
url: https://arxiv.org/abs/2609.28385
pdf_url: https://arxiv.org/pdf/2609.28385
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: LLM训练 · GRPO与蒸馏融合优化
tags:
- GRPO
- On-Policy Distillation
- Reinforcement Learning
- Credit Assignment
- Entropy Calibration
one_liner: 提出UECR-GRPO框架融合校验与教师信号，提升GRPO在推理任务上的训练效果
practical_value: '- 做Agent工具调用/推理路径优化的GRPO训练时，可借鉴PUU模块，将业务规则reward（如转化、点击率）和大模型教师的路径偏好提前融合再做组归一化，解决相同reward样本无法排序的问题

  - Token级信用分配时可复用ECR的熵校准+零和投影trick：用教师模型的token熵过滤不确定的指导信号，同时保证每个响应的总任务信用不变，避免引入额外偏差

  - 做蒸馏+RL混合训练时，不要直接叠加两个独立损失，优先在组归一化前融合信号，能减少梯度冲突、提升训练稳定性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
GRPO仅依赖最终结果的粗粒度reward，相同reward的样本无法区分，token级信用均匀分配导致错误步骤惩罚不到位；在线策略蒸馏（OPD）能提供稠密token级反馈，但教师信号不一定和最终正确性一致，现有方法把教师信号加在组归一化之后，无法影响响应排序，还可能改变总任务信用规模，带来偏差。

### 方法关键点
- 路径效用统一（PUU）：将校验器reward和长度归一化的教师分数融合成联合效用，再做组归一化，让教师信号能参与响应排序，同时保证任务reward的主导地位
- 熵校准再分配（ECR）：用教师与旧策略的token log概率差作为信用调整方向，用教师的全词表熵衰减不确定的指导，再通过响应级零和投影保证每个响应的总任务信用不变，仅在token间重新分配
- 把统一优势拆分为任务和教师分量，ECR只调整任务分量，避免干扰蒸馏信号

### 关键结果
在5个数学推理基准上测试，用Qwen3-1.7B和4B作为学生模型，对比Vanilla GRPO、Distilled RL、ATOD等SOTA基线：1.7B学生平均Avg@12达17.21%，超最强基线0.89个百分点；4B学生平均达65.09%，超最强基线0.56个百分点。

最值得记住的一句话：融合校验器和教师信号时，先联合再归一化比后加信号效果更好，token级信用分配要优先保证总任务信用不变，才能避免引入额外偏差。
