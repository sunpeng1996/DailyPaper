---
title: 'ProQuant: Progressive Quantization-aware Training for Edge MLLMs'
title_zh: ProQuant：面向边缘多模态大模型的渐进式量化感知训练框架
authors:
- Yufei Xue
- Yushi Huang
- Jiawei Shao
- Pingcheng Dong
- Yonghao Tan
- Shiyao Li
- Kwang-Ting Cheng
- Jun Zhang
affiliations:
- 香港科技大学
- 西北工业大学
- 中国电信TeleAI
- 清华大学
arxiv_id: '2611.08216'
url: https://arxiv.org/abs/2611.08216
pdf_url: https://arxiv.org/pdf/2611.08216
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: 多模态大模型 · 低比特量化感知训练
tags:
- Quantization
- QAT
- MLLM
- Edge Deployment
- Model Compression
one_liner: 提出面向边缘MLLM的低比特QAT框架，W4A8量化精度损失仅~1%，显著优于现有方案
practical_value: '- 端侧MLLM部署（如电商端侧多模态搜推Agent、AR交互理解）的W4A8量化场景，可直接复用SRL自标注方案：用待量化目标模型重生成训练标签，避免跨模型标注的分布
  mismatch，不需要依赖GPT-4等大模型标注，成本更低效果更好。

  - 多模态模型量化训练可借鉴PBA渐进块激活机制：先计算vision-sensitive因子识别多模态关键层，优先恢复多模态理解能力再逐步开放文本层量化，比全层同时量化收敛更快、最终精度更高，可迁移至多模态生成式推荐模型的低比特部署。

  - 量化方案选型可参考结论：W8A8场景下现有PTQ方法精度已达标，不需要额外做QAT节省训练成本；仅W4A8及更低比特量化需求时采用ProQuant方案性价比最高。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多模态大模型（MLLM）在端侧搜推、AR交互等场景落地价值高，但现有低比特量化方案在2B~8B边缘友好的小模型上精度损失严重，尤其是W4A8/W4A4等激进量化配置下多模态理解能力直接崩溃；传统QAT方案存在训练数据与预训练分布 mismatch、多模态与文本能力恢复优先级不清晰的问题，无法适配边缘MLLM部署需求。

### 方法关键点
- 自重标注（SRL）方案：抛弃开源多模态数据集原有标注，用待量化的目标模型重新生成响应标签，对齐微调数据与预训练分布，避免跨模型标注的风格差异带来的训练噪声。
- 渐进块激活（PBA）机制：通过vision-sensitivity因子τ计算每个Transformer层对视觉输入的梯度占比，识别多模态关键层；训练初期仅对视觉敏感层开启量化，随训练推进逐步开放文本敏感层量化，优先恢复多模态理解能力再优化文本生成能力。
- 推理侧无额外算子开销，支持W8A8/W4A8/W4A4/权重量化等多种配置，适配端侧硬件。

### 关键结果
在Qwen2-VL、Qwen2.5-VL、Qwen3-VL三个2B~8B模型上测试，对比SmoothQuant、MBQ、LLM-QAT等主流方案：
- W4A8配置下平均精度仅比全精度低~1%，比最优基线高2~6.6个百分点；
- W4A4配置下现有PTQ方案基本崩溃（准确率不足10%），ProQuant仍能保持54%~60%的平均准确率，比LLM-QAT基线高9~32.5个百分点；
- 端侧ASIC实测最高实现3.64倍prefill加速、5.64倍能耗降低。

### 核心结论
边缘MLLM低比特量化的核心优先级是先保住多模态理解能力再优化文本能力，数据分布对齐的收益远高于用更强的第三方标注模型。
