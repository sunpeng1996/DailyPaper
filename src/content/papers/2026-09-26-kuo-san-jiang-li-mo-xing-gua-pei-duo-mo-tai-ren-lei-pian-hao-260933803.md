---
title: Diffusion Reward Models
title_zh: 扩散奖励模型：适配多模态人类偏好的无参数奖励建模框架
authors:
- Xiangyang Wang
- Bingxiang He
- Zeyuan Liu
- Jiaze WangZiqing Qiao
- Yuxin Zuo
- Huan-ang Gao
- Cheng Qian
- Wenbin Zhang
- Ran Li
- Youbang Sun
affiliations:
- Tsinghua University
- The Chinese University of Hong Kong
- University of Illinois Urbana-Champaign
arxiv_id: '2609.33803'
url: https://arxiv.org/abs/2609.33803
pdf_url: https://arxiv.org/pdf/2609.33803
published: '2026-09-26'
collected: '2026-09-29'
category: Training
direction: LLM对齐 · 扩散奖励模型
tags:
- Reward Model
- Diffusion Model
- RLHF
- Human Preference
- DiT
one_liner: 用轻量DiT做无参数假设的奖励分布建模，适配多类标注数据，性能超越同规模基线
practical_value: '- 做Agent/生成式推荐的RLHF对齐时，可直接复用DRM的轻量DiT奖励头替换现有标量头，无需修改冻结的LLM编码器，训练成本低，同时可获取用户偏好的分布信息而非单一标量

  - 电商/推荐场景的多维度打分（相关性、有用性、合规性等）可复用DRM的统一训练框架，同时兼容多属性标注数据和pairwise偏好数据，无需维护多套独立模型

  - 推荐/广告的bad case防控可复用DRM的奖励分布统计量（方差、分位数），实现不确定性感知的候选过滤：对奖励方差过大的候选直接降权或拒绝，降低不符合预期的结果透出概率

  - 测试阶段可通过调整扩散采样数灵活trade-off推理精度与延迟，适配不同业务SLA：低延迟要求场景用少量采样，高精度要求场景增加采样数无需重新训练'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有奖励模型（RM）均默认输出标量或服从固定参数族的奖励分布，与人类偏好天然多模态、标注分歧大的特性冲突——LLM对齐数据集的标注一致性普遍仅60%-70%，标量奖励会丢失大量分歧、不确定性信息，易导致奖励黑客、对齐效果受限。

### 方法关键点
- 架构拆分：冻结LLM编码器输出prompt-response对的最后token隐状态，轻量Diffusion Transformer（DiT）作为扩散奖励头，条件建模奖励分布$p(r|x,y)$，无任何参数分布假设，天然适配多模态偏好
- 统一训练框架：同时支持两类标注数据，多属性回归任务用带mask的MSE去噪损失，pairwise偏好任务用去噪+Bradley-Terry联合损失，无绝对标注时可构造对称伪标签
- 推理灵活：通过DDIM采样N次得到经验奖励分布，可聚合为均值（兼容现有RLHF/排序逻辑）、方差、分位数，独有奖励轴测试时缩放能力，调整采样数可直接trade-off精度与延迟

### 关键结果
- 同骨干、同训练数据下，DRM-Multi-8B在5个公开RM基准的平均得分达66.2，比标量头ArmoRM高3.9分，比参数化分布头QRM高2.1分，性能接近GPT-4o等大参数量生成式裁判
- 下游RLHF用DRM作为奖励信号，MT-Bench得分从73.6提升至74.8，Arena-Hard v2得分从1.3提升至2.0
- 基于奖励方差做不确定性感知过滤，拒掉30%高不确定样本时，PPE任务平均精度提升2.81个百分点

人类偏好本质是多模态分布，仅用标量奖励会丢失大量有效信息，无参数分布建模是提升对齐效果的高性价比方向
