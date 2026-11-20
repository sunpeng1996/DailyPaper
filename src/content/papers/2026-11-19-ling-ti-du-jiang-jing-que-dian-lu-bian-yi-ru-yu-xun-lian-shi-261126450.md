---
title: 'A CPU Inside an LLM: Zero-Gradient Compilation of Exact Circuits into Pretrained
  Weights'
title_zh: 零梯度将精确电路编译入预训练权重，实现LLM内置确定性计算能力
authors:
- Tanmay Sah
affiliations:
- Independent Researcher
arxiv_id: '2611.26450'
url: https://arxiv.org/abs/2611.26450
pdf_url: https://arxiv.org/pdf/2611.26450
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM权重编译 · 确定性逻辑注入
tags:
- Zero-Gradient
- Circuit Compilation
- Pretrained LLM
- Deterministic Computation
- Weight Grafting
one_liner: 零梯度无需训练数据与外部工具，将算术与布尔电路编译入预训练LLM权重并保留原生语言能力
practical_value: '- 确定性规则注入：电商/导购Agent需要执行固定规则（如满减计算、优惠券核销）时，可借鉴零梯度权重嫁接思路，无需标注训练数据即可植入逻辑，避免微调带来的分布偏移，同时不影响原LLM的自然交互能力

  - 混合精度部署优化：业务部署LLM时，可将高频确定性逻辑用FP32单独做稀疏侧car，主干权重用INT4/INT8量化，兼顾规则执行精度与显存开销，参考文中显存降低42%-44%的实现方案

  - 触发鲁棒性优化：借鉴文中差分绑定嵌入+0触发漂移设计，优化Agent工具调用的触发逻辑，降低电商导购场景下规则误执行、工具误调用的概率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
预训练LLM在精确多位数算术、确定性规则执行上表现不稳定，现有方案要么需梯度微调引入分布偏移，要么依赖外部工具调用增加链路复杂度与延迟，无法满足端侧、隔离环境等受限场景下的确定性计算需求。
### 方法关键点
- 三类零梯度电路嫁接原语：Mellin-GLU积分抵消RMSNorm的250×动态范围波动，满足IEEE 754误差边界；带符号Chebyshev Indefinite-RoPE自陷注意力与无状态GatedDeltaNet偏移实现跨Token尺度抵消；轴对齐宽度扩展搭配√(d/(d+K))范数补偿，保证原生语言能力不退化，差分绑定嵌入实现零触发漂移。
- 5阶段自动化编译器，可将4-8位带符号±×电路、3变量布尔电路、5位多数/奇偶校验电路编译为LLM权重补丁，仅修改<0.06%的权重参数。
- 块稀疏侧car runtime方案，主干权重保持原生宽度，仅运行激活的电路切片，降低显存与延迟开销。
### 关键结果
在IBM Granite 3B、阿里Qwen 3.5 4B模型上验证，对比12.8K样本训练的LoRA方案：6位算术精度分别达99.17%、100%（LoRA仅42.2%/61.7%），inline续写准确率98%-100%（LoRA为0），OOD触发误判率为0，语言基准表现与原生模型无统计学差异；块稀疏侧car将A100显存占用降低42%-44%，2048 Token预fill延迟降低1.96-2.67倍。
### 核心结论
无需训练、无需外部工具的确定性逻辑权重注入方案，可在几乎不影响原模型能力的前提下为LLM植入规则化计算能力，是Agent、端侧LLM落地的重要技术路径。
