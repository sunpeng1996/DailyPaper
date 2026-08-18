---
title: 'Learn What''s Left, Not What''s Mastered: Saturation Aware Advantage Reweighting
  for Multi-Reward Policy Optimization'
title_zh: 面向多奖励策略优化的饱和度感知优势重加权方法
authors:
- Yixuan Wang
- Yifei Chen
- Haichao Zhang
- Haozheng Luo
- Xander Wu
- Jie Ni
- Yun Fu
- Nuno Vasconcelos
- Yijiang Li
affiliations:
- University of Florida
- UC San Diego
- Northeastern University
- Northwestern University
- Stanford University
arxiv_id: '2608.16072'
url: https://arxiv.org/abs/2608.16072
pdf_url: https://arxiv.org/pdf/2608.16072
published: '2026-08-16'
collected: '2026-08-18'
category: Training
direction: 多奖励RL训练 · 策略优化
tags:
- Multi-Reward RL
- GRPO
- Policy Optimization
- Saturation Awareness
- LLM Alignment
one_liner: 提出饱和度感知多奖励策略优化方法SA-MRPO，动态将优化资源倾斜至未饱和的难优化目标
practical_value: '- 做多目标LLM Agent对齐（如电商客服Agent需同时满足正确性、回复长度、合规性）时，可直接复用SA-MRPO的饱和度重加权逻辑，无需固定目标权重，自动将优化资源倾斜到难优化目标，如合规达标后自动提升回复正确率

  - 推荐系统多目标RL排序（同时优化点击率、转化率、停留时长、负反馈）时，可将饱和度计算适配到各目标的业务值域，动态调整梯度权重，避免已饱和的CTR目标占用过多优化资源

  - 工程改造成本极低：无需修改原有GRPO/GDPO训练框架，仅需在优势计算模块新增基于batch平均奖励的饱和度计算和重加权逻辑即可

  - 超参数γ可直接控制业务目标权衡：优先保证已达标目标稳定性可设小γ，攻坚难优化目标推荐设0.25-0.5的中等值'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多奖励策略优化方法大多先对多维度奖励做固定权重加权求和，再做组内标准化，存在两个核心缺陷：一是不同奖励分布的样本可能得到相同标量奖励，丢失奖励分辨率；二是固定权重忽略目标饱和度，会持续为已经优化到接近上限的目标分配梯度资源，反而忽略还有很大提升空间的难优化目标，导致训练效率低、核心业务指标提升困难。

### 方法关键点
- 每个奖励目标单独做组内标准化，保留各维度奖励的相对信息，避免标量融合的信息损失
- 新增batch级饱和度计算：用当前batch的平均奖励与该目标值域上下限的比值得到饱和度s(k)，越接近1代表目标优化越充分
- 动态调整目标权重：每个目标的实际权重为原始权重乘以(1-s(k))^γ，γ为饱和度指数，值越大对饱和目标的权重打压越强
- 聚合各维度标准化优势后再做全局标准化，直接接入原有GRPO损失函数，无需修改其他训练逻辑，GDPO/GRPO均为SA-MRPO的特例

### 关键实验
跨数学推理、自适应推理、代码生成3个场景验证，对比baseline为GDPO：15个数学推理benchmark中12个正确率优于GDPO，AIME24最高提升5%；自适应推理5个benchmark全部优于GDPO，平均提升3.8%，AMC23最高提升9.2%；代码生成场景测试集通过率最高提升2.3%，已饱和的可执行性指标几乎无下降。

**最值得记住的一句话：** 多目标优化的核心不是平均分配资源，而是把算力集中在还能产生增量价值的目标上。
