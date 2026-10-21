---
title: Robust Direct Preference Optimization under Preference Label-Flip Attacks
title_zh: 偏好标签翻转攻击下的鲁棒直接偏好优化方法
authors:
- Chenye Yang
- Weiyu Xu
- Lifeng Lai
affiliations:
- University of California, Davis
- University of Iowa
arxiv_id: '2610.24945'
url: https://arxiv.org/abs/2610.24945
pdf_url: https://arxiv.org/pdf/2610.24945
published: '2026-10-18'
collected: '2026-10-21'
category: Training
direction: 大模型对齐 · 鲁棒DPO训练
tags:
- DPO
- RLHF
- Adversarial Attack
- Robust Training
- Label Flip
one_liner: 提出Trim-K与Soft-Trim-K鲁棒DPO算法，可抵御偏好标签翻转攻击并提供理论保障
practical_value: '- 生成式推荐/Agent的DPO对齐场景中，若存在恶意标注、刷分等标签污染问题，可先计算每个偏好对的梯度影响得分，删除/降权Top
  K高影响样本，大幅降低污染数据的干扰

  - 不确定攻击/噪声规模时优先选用Soft-Trim-K的指数降权方案，通过τ超参数灵活调节鲁棒性与数据利用率的平衡，避免硬删带来的有效数据损失

  - 对合规性要求高的业务场景（如电商营销文案生成、客服Agent对齐），可在Trim/Soft-Trim基础上叠加参考参数L2正则，进一步控制攻击导致的参数漂移，仅需承受少量干净数据上的精度损失'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
DPO作为离线RLHF的核心对齐方法，已广泛应用于大模型、生成式推荐等场景，但其高度依赖标注的成对偏好数据，极易遭到针对性标签翻转攻击（恶意篡改样本优劣顺序），少量攻击即可让对齐后的模型偏向攻击者指定的有害策略，现有鲁棒方案大多仅处理随机标注噪声，无法应对对抗性攻击，存在严重的安全隐患。
### 方法关键点
- 基于log-linear DPO的核心性质：单样本标签翻转带来的梯度偏移与模型参数无关，可提前计算每个偏好对的翻转影响得分$s_i=\beta\|v_i\|_2$（$v_i$为正负样本的特征差）
- 提出Trim-K Robust-DPO：直接删除得分最高的K个偏好对，从根源上规避高影响样本被攻击后的梯度污染，无攻击时K=0退化为标准DPO
- 提出Soft-Trim-K Robust-DPO：对Top K高影响样本按指数规则降权而非硬删，通过温度τ调节降权强度，平衡数据保留率与鲁棒性
- 可叠加参考参数附近的L2正则项，提升优化曲率，进一步限制攻击后的参数漂移，同时明确给出所有方法的梯度、参数、策略偏差的理论边界
### 关键实验
在SHP、HH-RLHF、UltraFeedback-Binarized三个公开偏好数据集上测试，对比标准DPO、正则DPO等基线：30%高影响样本标签翻转攻击下，Trim-K将策略与干净DPO的KL散度从0.155降至0.018，Soft-Trim-K降至0.064；定向BMP-A攻击下，带正则的Trim-K比同正则强度的标准DPO KL降低9.3%。
### 核心结论
高梯度影响的偏好对是DPO对齐的核心风险点，提前过滤或降权这类样本的工程实现成本极低，可同时提升DPO对对抗攻击和随机标注噪声的防御能力。
