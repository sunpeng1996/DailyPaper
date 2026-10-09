---
title: 'CARE: Certifying Acceleration for Vision-Language-Action Inference'
title_zh: CARE：视觉-语言-行动模型推理的可认证加速框架
authors:
- Rui Liu
- Tong Zheng
- Jindong Gu
- Zhipeng Wang
affiliations:
- University of Maryland, College Park
- University of Oxford
- Google
arxiv_id: '2610.08917'
url: https://arxiv.org/abs/2610.08917
pdf_url: https://arxiv.org/pdf/2610.08917
published: '2026-10-05'
collected: '2026-10-09'
category: Agent
direction: Agent推理加速 · 风险可控选型
tags:
- Inference Acceleration
- VLA
- LLM Agent
- Risk Control
- Sequential Testing
one_liner: 提出可认证的Agent推理加速选型框架，在控制加速诱导失败率前提下最大化速度提升
practical_value: '- 复用failure-triggered reference rollout思路，做LLM/GenRec加速方案选型时，仅在轻量加速版失效的case上跑原版大模型评测，大幅降低评测成本

  - 借鉴任务均衡序贯检验+最快优先的选型逻辑，在KV cache、剪枝、动态步长等推理加速方案选型时，快速锁定满足业务风险预算的最快方案，无需全量评测所有候选

  - 复用AIF（加速诱导失败）量化指标，替代单纯平均准确率，更精准衡量加速方案对业务效果的负向影响，避免平均指标掩盖部分场景的效果退化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
VLA/LLM类Agent的推理成本是落地核心瓶颈，现有加速方案（action chunking、token剪枝、特征缓存等）仅用平均成功率和latency评估，会掩盖「原模型可解决但加速后失败」的退化问题；且闭环决策下动作偏差会累积，单步指标无法反映全episode的真实风险，亟需可量化控制退化风险的加速选型方法。

### 方法关键点
- 定义AIF（加速诱导失败）损失：相同初始条件下原模型成功、加速后失败的episode作为负样本，避免平均指标中「加速新解决的任务抵消退化任务」的问题
- 离线校准流程：先对所有加速候选按latency从快到慢排序，在calibration集上做任务平衡的轮次评测，用随时有效的e-process做序贯检验，满足风险预算立即返回，无需测完全量样本
- 校准成本优化：仅当加速候选失败时才运行原模型评测，结果缓存复用，大幅减少原模型的rollout次数

### 关键实验
在LIBERO机器人任务集测试OpenVLA-OFT，对比latency优先、平均成功率匹配、验证集调优等基线：CARE实现9.0~10.8×加速，95%置信度下保留至少85.8%的原模型成功episode；紧风险预算下其他基线超预算比例达13%~75%，CARE始终不超预算，校准rollout次数比全量评测少78.9%，还可扩展到π0.5、Qwen3.5-9B、Llama3.1-8B等Agent的加速选型。

### 核心结论
加速选型不能只看速度和平均准确率，要通过配对全episode评测量化控制业务不可接受的退化风险，同时可通过序贯检验和懒加载原模型评测大幅降低选型成本
