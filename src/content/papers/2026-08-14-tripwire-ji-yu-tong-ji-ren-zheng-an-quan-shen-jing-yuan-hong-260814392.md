---
title: 'Tripwire: Triggering Aligned Refusal via Statistically Certified Safety Neurons'
title_zh: Tripwire：基于统计认证安全神经元触发LLM对齐拒绝响应
authors:
- Wei Zhao
- Zhe Li
- Peixin Zhang
- Jun Sun
affiliations:
- Singapore Management University
arxiv_id: '2608.14392'
url: https://arxiv.org/abs/2608.14392
pdf_url: https://arxiv.org/pdf/2608.14392
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: LLM安全 · 神经元级越狱防御
tags:
- LLM Safety
- Jailbreak Defense
- Neuron Intervention
- Training-free
- Statistical Filtering
one_liner: 无需训练的LLM越狱防御框架，平均攻击成功率降至2%以下，效用损失为同类方案最低
practical_value: '- 业务LLM（客服、文案生成、Agent推理模块）的越狱防御可直接复用该统计筛选安全神经元的流程，无需重新训练模型，落地成本低

  - 两种部署模式可按需选择：推理侧网关模式适合需保留原模型全部能力的场景（如商品文案生成、用户咨询应答），离线权重补丁模式适合无网关、低延迟要求的端侧/嵌入式Agent场景

  - 神经元筛选的FDR控制+效用特异性过滤思路可迁移到其他神经元级干预任务（如LLM对齐微调后保留特定业务能力、定向消除模型幻觉）'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM神经元级越狱防御存在三大痛点：擦除式干预需覆盖大量分散的有害语义路径，效用损失高；基于外部分类器的安全神经元识别无法区分安全专属与通用重要神经元；常驻式干预会扰动所有正常请求，即使无攻击发生，亟需低效用损失的高精度防御方案。
### 方法关键点
- 统计筛选漏斗：依次经过3层过滤：方向过滤（有害样本激活均值> benign样本）、Welch t-test+BH-FDR控制假阳性率、效用特异性过滤（排除正常任务激活过高的神经元），最终按AUROC排序选Top-N安全神经元
- 触发式钳位：将选中神经元固定为有害输入下的平均激活值，主动注入“输入有害”内部信号，触发模型对齐阶段已习得的拒绝行为，无需拦截所有有害路径
- 两种等价部署模式：推理侧网关模式（仅对检测到的有害请求触发钳位，正常请求无修改）、离线权重补丁模式（直接修改权重实现永久钳位，无推理额外开销）
### 关键实验
在4个安全对齐开源LLM（Llama2-7B、Llama3.1-8B、Qwen2.5-7B/32B）上，对抗4种主流越狱攻击，对比RepE、TraceRouter等SOTA防御基线：平均攻击成功率降至≤2.0%，远低于基线的2.2%~12.6%；MT-Bench效用损失仅0.5%~5.3%，为所有防御中最低，推理开销仅1.15x。
### 核心洞见
神经元级防御的效用损失核心源于神经元筛选精度不足和常驻干预，而非神经元级干预本身，严格统计筛选+按需触发可实现最优安全-效用权衡。
