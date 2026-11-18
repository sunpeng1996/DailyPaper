---
title: 'Beyond Bitwidth: Deployment-Constrained Mixed-Precision Quantization for Multilingual
  LLM Inference on NVIDIA Blackwell'
title_zh: 面向NVIDIA Blackwell的多语言LLM部署约束混合精度量化
authors:
- Hyojung Han
affiliations:
- ThakiCloud
arxiv_id: '2611.21974'
url: https://arxiv.org/abs/2611.21974
pdf_url: https://arxiv.org/pdf/2611.21974
published: '2026-11-16'
collected: '2026-11-18'
category: LLM
direction: LLM量化 · 部署端落地优化
tags:
- Quantization
- LLM Inference
- NVIDIA Blackwell
- vLLM
- Mixed Precision
- Multilingual LLM
one_liner: 在NVIDIA B200上实测多语言LLM量化失效模式，输出满足多约束的可部署混合精度配置
practical_value: '- 量化验证不要仅看标称位宽和通用benchmark，必须叠加业务实际约束（特定语言精度、首包延迟、实际加载内存、vLLM内核兼容性），避免开发集效果达标但上线失效

  - 混合精度分配不要迷信单模块灵敏度排序，不同任务（生成/推理、多语言/英文）的敏感模块相关性极低，修复效果非加性，必须全量验证组合效果

  - 采用NVFP4量化时优先选择W4A16（16位激活）而非W4A4，精度提升显著，配合INT8量化输出头可节省内存刚好卡进显存阈值，平衡精度与延迟

  - 多语言LLM校准不要盲目增加目标语言样本，可能损失推理等其他能力，必须覆盖所有业务关心的任务维度做联合验证'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有低比特LLM量化研究多聚焦压缩率与通用指标，忽略部署端实际约束（内核兼容性、实测加载内存、业务特定精度要求、延迟限制），导致实验室表现优异的方案上线后不可用，尤其多语言场景下小语种精度退化、生成任务崩坏的问题突出，亟需端到端的部署约束下量化验证与选型方案。

### 方法关键点
- 实验基于Qwen3-8B，在NVIDIA B200 + vLLM 0.29.0环境下测试INT2/INT3/GPTQ/NVFP4等量化格式，以fused线性模块为最小精度分配单位
- 预设4项硬约束：所有模块运行指定packed内核、权重加载内存<5.98GiB、韩/英/数值/推理4维度精度保留率≥0.9、TPOT不超过BF16的1.1倍
- 实验流程分为诊断集测模块灵敏度、选择集筛选候选、独立终测集验证三阶段，全程冻结规则避免选择偏差

### 关键结果
- INT2所有7种量化网格均出现生成任务完全崩坏（100%循环/截断），INT3精度远低于阈值，仅可作为辅助压缩方案
- 最优配置A81：16位激活+98个NVFP4权值模块+46个INT8保护模块+INT8输出头，实测权重内存5.917GiB，韩语精度保留率0.904，TPOT为BF16的0.939倍，所有约束全部达标
- A81比NVFP4 W4A4基线精度高1.4pp（Bonferroni调整后置信区间[+0.2, +2.6]），精度提升主要来自16位激活的贡献

**最值得记住的一句话**：LLM量化部署是数值优化与系统工程的联合问题，验证协议对不合格方案的筛选价值，远高于量化格式本身的理论优势
