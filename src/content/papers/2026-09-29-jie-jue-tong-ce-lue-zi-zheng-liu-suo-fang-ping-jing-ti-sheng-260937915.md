---
title: Overcoming Scaling Limits in On-Policy Self-Distillation for LLM Reasoning
title_zh: 解决同策略自蒸馏缩放瓶颈 提升大模型数学推理能力
authors:
- Md. Ismail Hossain
- Humaira Kousar
- Isidora Chara Tourni
affiliations:
- North South University
- KAIST
- Andria Labs
arxiv_id: '2609.37915'
url: https://arxiv.org/abs/2609.37915
pdf_url: https://arxiv.org/pdf/2609.37915
published: '2026-09-29'
collected: '2026-09-30'
category: Training
direction: LLM训练 · 自蒸馏推理性能优化
tags:
- self-distillation
- on-policy
- LLM-reasoning
- scaling
- OPSD
one_liner: 提出仅需最终答案标签的OASIS自蒸馏方法，解决OPSD随模型规模扩大效果衰减问题
practical_value: '- 可直接复用「仅对最终验证通过的轨迹做蒸馏」的思路到生成式推荐、Agent推理优化场景，无需完整过程标注，仅用可验证的业务结果（如转化、答对）即可做自蒸馏，大幅降低标注成本

  - 针对推荐系统的用户行为序列建模，可过滤未产生最终转化的无效浏览路径噪声，仅对转化路径的行为序列做蒸馏，提升序列建模的有效性

  - 做大模型落地的团队可优先选择OASIS类可缩放自蒸馏方案，避免OPSD在小模型上验证有效、大模型上增益几乎归零的问题，适配7B/14B等主流部署规模'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有On-policy Self-Distillation（OPSD）方法优化LLM推理能力存在两大痛点：一是依赖完整的推理过程标注，仅能用于有标准答案的有限场景；二是增益随模型规模扩大快速衰减，在8B参数规模下相对基准模型仅提升0.14个点，几乎失效，无法适配大模型的缩放需求。
### 方法关键点
- 提出OASIS方法，保留OPSD的前向KL损失函数不变，仅调整监督轨迹选择逻辑：每个问题采样K条rollout，仅对最终答案验证通过的轨迹做蒸馏，优先选择最短的验证轨迹作为训练骨架，降低无效计算
- 教师端上下文不再使用人工标注的完整参考答案，替换为同问题下模型生成的未验证rollout，仅需最终答案标签即可完成训练，无需过程标注
- 从理论上证明OPSD存在不可约模仿间隙，核心来自教师的特权信息，且该间隙仅存在于未验证轨迹上，验证轨迹上的教师信号对上下文不敏感，无需特权信息即可获得有效监督
### 关键实验
基于Qwen3-1.7B/4B/8B三个参数规模的模型，在AIME 2024、AIME 2025、HMMT2025三个数学推理基准上测试，对比OPSD、GRPO、SFT等基线：OASIS相对基准模型平均提升3.2~3.8个点，增益不随模型规模扩大衰减；8B规模下相对OPSD提升3.05个点，远高于OPSD的0.14个点增益；仅需1/4的监督样本量即可达到或超过OPSD的效果，仅额外付出多采样rollout的推理成本。
### 最值得记住的结论
同策略自蒸馏的有效监督信号仅来自验证通过的轨迹，未验证轨迹的特权信息带来的模仿间隙会随模型规模扩大完全抵消训练增益
