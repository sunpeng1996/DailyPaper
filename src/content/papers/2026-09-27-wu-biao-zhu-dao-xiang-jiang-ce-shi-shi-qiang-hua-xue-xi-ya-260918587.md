---
title: 'Label-free steering: Compressing test-time reinforcement learning into bias-only
  subspaces'
title_zh: 无标注导向：将测试时强化学习压缩到仅偏置参数子空间
authors:
- Naveen Vakada
- Mingyuan Li
- Shaoxiong Ji
affiliations:
- University of Turku, Finland
- ELLIS Institute Finland
arxiv_id: '2609.18587'
url: https://arxiv.org/abs/2609.18587
pdf_url: https://arxiv.org/pdf/2609.18587
published: '2026-09-27'
collected: '2026-10-01'
category: Training
direction: 参数高效训练 · 无标注测试时RL自适应
tags:
- Test-time RL
- Parameter Efficient Tuning
- Bias-only Steering
- Label-free Learning
- GRPO
one_liner: 仅优化约100K偏置参数，用无标注多数投票奖励实现跨模态高效测试时自适应
practical_value: '- 电商/推荐场景的LLM适配可复用「多数投票伪标签+GRPO」范式，无需标注数据即可快速对齐业务需求，仅优化偏置参数的训练成本比全微调低16倍以上

  - 小参数量微调选型时可优先尝试仅优化MLP层偏置的方案，同参数预算下效果优于LoRA，且训练更稳定，无ReFT这类方法的后期性能退化问题

  - 训练得到的偏置向量可直接迁移到同领域的未见任务，比如商品理解、Query改写场景训练的偏置，可直接套用到新类目的同类任务，无需重训即可拿收益

  - 落地时需审计伪标签的可靠性，避免模型学到数据集模板捷径而非真实能力，尤其要校验推荐文案生成、搜索Query改写的输出合理性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有测试时强化学习（TTRL）通常需要优化全量或大量模型参数，且高度依赖标注奖励，在推理部署场景下的算力、标注成本过高，业界亟需验证极端参数限制下，无标注测试时自适应的可行性。

### 方法关键点
- 冻结预训练大模型全部主干参数，仅优化各Decoder层MLP的偏置参数，7B模型仅约100K可训练参数，为全参数微调的1/76000
- 奖励完全无标注：对每个输入采样多轮生成结果，取答案的多数投票结果作为伪标签，符合伪标签的生成给+1奖励，否则给-1
- 用GRPO计算组归一化优势，无需额外训练价值函数，梯度仅反向传播到偏置参数，训练内存开销极低

### 关键结果
- 在文本、视觉语言、音频三类推理任务上均超过基线：Qwen2.5-7B在MATH-500上准确率达76.67%，仅比全参数微调低0.33个百分点，训练GPU耗时降低16~18.5倍
- 同100K参数预算下，偏置优化效果全面超过LoRA、ReFT等参数高效微调方案，且无训练后期性能退化问题
- 学到的偏置向量可直接迁移到4500个未见过的MATH问题，Qwen2.5-7B准确率从46.3%提升至70.9%，泛化性强

### 核心结论
可训练子空间与优化梯度的对齐度，比参数量本身更决定小预算下的自适应效果，仅优化偏置的无标注TTRL可以用极低成本拿到接近全微调的收益
