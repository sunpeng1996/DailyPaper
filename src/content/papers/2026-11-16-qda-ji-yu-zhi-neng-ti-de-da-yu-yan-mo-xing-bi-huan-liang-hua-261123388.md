---
title: 'QDA: Closed-Loop LLM Quantization Design with Agents'
title_zh: QDA：基于智能体的大语言模型闭环量化设计系统
authors:
- Xingyang Li
- Tianlang Zhao
- Song Han
- Ligeng Zhu
affiliations:
- MIT
- NVIDIA
arxiv_id: '2611.23388'
url: https://arxiv.org/abs/2611.23388
pdf_url: https://arxiv.org/pdf/2611.23388
published: '2026-11-16'
collected: '2026-11-19'
category: Agent
direction: Agent 优化 LLM 低精度量化部署
tags:
- LLM Quantization
- Post-Training Quantization
- LLM Agent
- Low-Precision Inference
- MoE
- KL Divergence
one_liner: 用LLM Agent自动搜索适配不同模型与精度的PTQ量化配方，提升低精度推理准确率且无额外开销
practical_value: '- 可复用其低精度模型快速评估方案：用预缓存原模型top-k分布的KL散度作为代理指标，比全量评估快350~990倍，大幅提升推荐场景常用LLM（召回排序、文案生成、query理解类）的量化迭代效率

  - 量化配方自动搜索框架可迁移到业务场景：针对垂域微调的业务专属LLM自动组合不同PTQ方法找最优配方，无需专家手动调参，降低部署成本

  - 可组合PTQ方法库的设计思路可复用：统一21种PTQ方法的输入输出接口，支持跨模型架构堆叠组合，适配MoE等新结构，可直接集成到现有LLM部署工具链

  - 量化模型无推理overhead的设计思路值得借鉴：生成的量化checkpoint完全兼容vLLM等现有推理内核，无需修改业务现有推理服务即可替换，落地成本低'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
Post-training quantization（PTQ）是LLM低成本部署的标准方案，但最优量化配方随模型结构、精度要求差异极大，专家手动设计效率低、难以适配快速迭代的新模型。现有自动化搜索方案存在两大痛点：单个量化候选的全量推理评估需数十GPU小时，不同PTQ方法代码不兼容需手动适配新架构，落地成本极高。
### 方法关键点
- 快速代理评估：预缓存原模型在推理trace上的top-128 token分布，用候选模型与原模型的输出KL散度作为准确率代理指标，单候选评估仅需数分钟，成本降低350~990倍；同时对高潜候选做长生成校验，避免重复循环等罕见错误
- 可组合PTQ方法库：统一21种主流PTQ方法的输入输出接口，支持任意顺序堆叠，自动适配新模型架构无需手动修改，MoE模型的GPTQ构建速度从16 GPU小时压缩到0.42 GPU小时
- 闭环Agent搜索流：Agent在沙箱内迭代提出量化配方，系统自动完成构建、评估、反馈，全程隔离测试集与参考trace避免过拟合，仅最终候选做全量测试
### 关键结果
测试覆盖4种主流推理模型（含MoE结构）以及320B参数的GLM-5.3-Flash MoE模型，对比GPTQ、AWQ、ParoQuant、GSQ等SOTA公开配方：W4A16、W4A8、W3A16精度下平均准确率较最强公开配方分别提升0.9、1.4、2.2个百分点，单搜索仅消耗64 GPU小时；320B GLM-5.3-Flash在NVFP4 W4A4精度下恢复FP8模型98.3%的准确率，优于厂商最优checkpoint的96.9%，且所有量化checkpoint完全兼容现有推理内核，无任何推理 overhead。
最值得记住的一句话：**针对特定模型/场景自动化搜索适配的低精度量化配方，比通用SOTA量化方法能获得更高的准确率与性能收益**
