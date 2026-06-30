---
title: One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline
  Parallel LLM Pretraining
title_zh: 一步梯度延迟并非大规模异步流水线并行LLM预训练的障碍
authors:
- Philip Zmushko
- Egor Petrov
- Nursultan Abdullaev
- Mikhail Khrushchev
- Samuel Horváth
affiliations:
- Institute of Science and Technology Austria (ISTA)
- Yandex
- Basic Research of Artificial Intelligence Laboratory (BRAIn Lab)
- Innopolis University
- Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)
arxiv_id: '2606.30634'
url: https://arxiv.org/abs/2606.30634
pdf_url: https://arxiv.org/pdf/2606.30634
published: '2026-06-29'
collected: '2026-06-30'
category: Training
direction: LLM预训练 异步流水线并行优化
tags:
- Asynchronous Pipeline Parallelism
- LLM Pretraining
- Optimization
- Muon
- Gradient Staleness
one_liner: 证明异步流水线并行的一步梯度延迟性能退化依赖优化器选择，配合Muon+误差反馈可对齐同步训练质量
practical_value: '- 训MoE大模型用流水线并行时，可选择PipeDream-2BW固定一步延迟调度，配合Muon优化器，既能消除流水线气泡提升GPU利用率，也不损失模型精度

  - AdamW对梯度延迟非常敏感，Muon等现代高动量优化器天然对梯度延迟鲁棒，大规模异步训练优先选Muon而非传统AdamW

  - 仅需额外增加一份模型参数大小的存储buffer，加上Error Feedback修正就能把同步异步的损失Gap缩小50%-90%，工程实现简单 overhead极低

  - 多stage深流水线场景下，固定延迟调度比原PipeDream的可变延迟鲁棒性好得多，大规模部署优先选固定延迟方案'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：大规模LLM尤其是MoE模型预训练越来越依赖流水线并行，同步流水线存在气泡浪费GPU算力，异步流水线虽然能消除气泡提升吞吐量，但业界普遍认为梯度延迟会导致训练不稳定、模型性能退化，一直未被大规模采用；PipeDream-2BW虽能提供固定一步梯度延迟，但其在LLM预训练中的实际效果缺乏系统验证。

**方法关键点**：
- 系统验证不同优化器对一步梯度延迟的鲁棒性，证明性能退化高度依赖优化器选择，而非梯度延迟本身的固有缺陷
- 发现核心规律：动量系数越高，优化器对梯度延迟的鲁棒性越强，AdamW这类传统低动量优化器退化严重，Muon等现代优化器天然鲁棒
- 提出优化器无关的Error Feedback修正方法，仅需额外存储一份历史更新，就能在不改变原有超参数的前提下缩小同步异步性能Gap
- 给出了Muon在一步梯度延迟下的收敛性理论保证

**关键实验**：在FineWeb-Edu数据集上实验，360M模型上Muon本身的同步异步损失Gap仅为0.012，远小于AdamW的0.278；加入Error Feedback后可恢复50%-90%的性能损失；10B参数MoE模型训练200B tokens后，异步+Error Feedback的最终验证损失和同步baseline完全一致（均为1.906）；16stage深流水线场景下，原PipeDream可变延迟的损失增加超过0.03，固定延迟方案可控制Gap在可接受范围。

**核心结论**：选择合适的优化器和调度，一步梯度延迟不会成为大规模异步流水线并行LLM预训练的障碍
