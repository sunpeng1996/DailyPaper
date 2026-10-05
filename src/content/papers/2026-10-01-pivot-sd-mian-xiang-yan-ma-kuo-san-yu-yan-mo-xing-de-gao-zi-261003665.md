---
title: 'Pivot-SD: Efficient Self-Distillation for Masked Diffusion Language Models'
title_zh: Pivot-SD：面向掩码扩散语言模型的高效自蒸馏框架
authors:
- Seo Hyun Kim
- Sunwoo Hong
- Younwoo Choi
- Chen-Hao Chao
- Se-Young Yun
- Rahul G. Krishnan
affiliations:
- KAIST AI
- University of Toronto
- Vector Institute
arxiv_id: '2610.03665'
url: https://arxiv.org/abs/2610.03665
pdf_url: https://arxiv.org/pdf/2610.03665
published: '2026-10-01'
collected: '2026-10-05'
category: Training
direction: 扩散语言模型 · 高效自蒸馏训练
tags:
- Self-Distillation
- Diffusion Language Model
- Pivot Selection
- Credit Assignment
- Efficient Training
one_liner: 通过信息增益筛选高影响pivot token，仅对其做正负监督，小样本下高效提升扩散LM推理能力
practical_value: '- 生成式推荐/Agent微调时，可复用pivot筛选逻辑，仅监督能大幅降低后续生成不确定性的关键token，无需全序列训练，降本提效

  - 优化失败生成轨迹时，仅对关键pivot施加unlikelihood损失，避免误伤正确的中间生成内容，适合文案、query生成、推理类场景的小样本调优

  - 小样本训练场景优先选离线自蒸馏范式，比在线RL更稳定，无需频繁推理采样，算力开销降低40%以上，适合业务端快速迭代

  - 非自回归并行生成场景（如电商批量文案生成、query联想）可直接复用信息增益计算pivot的方法，实现高效模型调优'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
掩码扩散语言模型（dLM）作为自回归模型的并行替代方案，推理速度优势突出，但现有后训练方案存在明显缺陷：要么对全序列token同等加权训练，要么给整个去噪步骤分配整体奖励，没有利用到去噪过程中少量关键commitment会大幅降低剩余位置不确定性、决定最终生成效果的特性，训练效率极低，失败轨迹的有效信息无法被充分利用，小样本下效果提升十分有限。
### 方法关键点
- 定义信息增益指标，衡量每一步去噪commitment对剩余掩码位置的平均熵降，选取Top-K高信息增益步骤对应的token作为pivot，熵计算复用采样阶段已有的前向pass，无额外推理开销
- 采用离线自蒸馏范式：先从冻结基模型采样生成轨迹，用验证器标注轨迹最终正确性，仅对pivot施加监督：正确轨迹的pivot用交叉熵损失强化，错误轨迹的pivot用unlikelihood损失弱化，其余token不参与损失计算
- 训练时回放pivot被提交时的部分掩码状态，保证监督上下文与生成时完全一致，避免分布偏移
### 关键实验
- backbone覆盖LLaDA-8B-Instruct、Dream-7B两款扩散LM，仅用200条训练样本、每条4次采样，在MATH、GSM8K、HumanEval+、MBPP+四个推理基准上测试
- 对比全序列SFT、预算匹配的diffu-GRPO、wd1++等RL基线，Pivot-SD平均精度最高，效果优于用10倍训练数据、5倍训练步数的RL基线，训练耗时仅为5000步diffu-GRPO的1/8，FLOPs比预算匹配RL低40%
- 跨backbone、跨领域迁移效果稳定，OOD平均精度比基线高0.8~1.8个点
### 核心结论
生成轨迹中仅不到4%的关键token决定最终效果，针对性监督这些token可以用远低于全序列训练的成本获得更优的效果
