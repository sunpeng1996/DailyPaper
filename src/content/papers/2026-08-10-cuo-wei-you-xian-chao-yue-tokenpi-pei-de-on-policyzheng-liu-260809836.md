---
title: 'Mismatch Matters: On-Policy Distillation Beyond Token Agreement'
title_zh: 错位优先：超越Token匹配的On-Policy蒸馏优化方法
authors:
- Zichao Yu
- Chengzhi Yu
- Shengze Xu
- Yujin Han
- Bingqing Jiang
- Xu Wang
- Difan Zou
affiliations:
- The University of Hong Kong
- University of Science and Technology of China
- The Chinese University of Hong Kong
arxiv_id: '2608.09836'
url: https://arxiv.org/abs/2608.09836
pdf_url: https://arxiv.org/pdf/2608.09836
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: LLM On-Policy蒸馏 训练稳定性优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- LLM Training
- TIDE
- Mathematical Reasoning
one_liner: 提出TIDE双分支矫正机制，解决On-Policy蒸馏的退化匹配问题，提升小模型蒸馏效果与稳定性
practical_value: '- 垂直领域小模型蒸馏（电商客服Agent、导购生成小模型）场景可直接复用TIDE双分支设计：对学生冗余生成token做Hellinger有界抑制，同时直接蒸馏教师top-K高概率token，避免采样遗漏，解决生成重复/冗长问题

  - 生成式推荐场景下用大模型蒸馏小模型做文案、item title生成时，可借鉴「忽略匹配token、仅矫正错位token」的思路，降低训练计算量，避免退化生成（重复营销话术、超长无意义文案）

  - Agent思考模块蒸馏训练时，可参考其token mismatch量化方法，优先给高错位token分配梯度预算，提升蒸馏效率，减少无效更新'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
On-Policy蒸馏（OPD）是当前LLM后训练的核心组件，但存在退化匹配失效模式：学生通过生成重复循环，在token级和教师达到近完美匹配，但全局响应完全无效，传统聚焦token匹配的优化思路完全失效，还伴随生成长度爆炸、格式错误率高等问题，严重影响蒸馏效果。

### 方法关键点
- 先将师生token错位分为两类：学生多余token（学生生成但教师概率接近0，log比无界导致更新不稳定）、学生缺失token（教师偏好但学生几乎不会采样，无法通过常规on-policy采样获得监督信号）
- 提出TIDE双分支矫正机制：
  1. 多余分支：对采样到的高错位多余token，用有界Hellinger shaping替换无界log比，避免梯度爆炸，仅优化前20%最严重的错位token
  2. 缺失分支：直接取教师top-K候选token做显式概率矫正，不需要等待学生采样到这些token，同样仅优化前20%最严重的缺失位置
  3. 匹配token完全不加入损失计算，节省梯度预算

### 关键实验
在9个数学推理基准测试，用Qwen3系列师生对对比GRPO、标准OPD、FiRe-OPD等6个SOTA基线：强错位场景（8B教师蒸馏1.7B学生）下，Avg@8从标准OPD的6.9%提升到20.3%，平均响应长度从22395token降到7294token，格式错误率从65.5%降到5.4%；弱错位场景下，Avg@8比标准OPD高1个点，Pass@8高3.2个点。

**最值得记住的一句话**：On-Policy蒸馏的监督信号应该优先分配给有信息差的错位token，而非已经匹配的token，且要根据错位方向的可观测性分别设计矫正机制。
