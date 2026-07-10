---
title: 'Teaching LLMs a Low-Resource Language: Enhancing Code Completion in Pharo'
title_zh: 低资源编程语言Pharo的大模型代码补全能力增强方案
authors:
- Kilian Kier
- Alessandro Giagnorio
- Omar AbedelKader
- Oleksandr Zaitsev
- Robert Peharz
- Romain Robbes
- Gabriele Bavota
- Stéphane Ducasse
affiliations:
- Graz University of Technology
- Università della Svizzera italiana
- Inria
- CNRS
- CIRAD
arxiv_id: '2607.04939'
url: https://arxiv.org/abs/2607.04939
pdf_url: https://arxiv.org/pdf/2607.04939
published: '2026-07-05'
collected: '2026-07-10'
category: Training
direction: 低资源场景 LLM 专项适配训练
tags:
- Low-resource LLM
- Code Completion
- Continual Pre-training
- Fine-tuning
- Benchmark
one_liner: 提出低资源语言代码补全全流程及专属基准，小参数量专项模型性能超通用大模型
practical_value: '- 低资源场景（小语种电商、小众品类推荐）可复用「领域数据 curated + 小参数量模型继续预训练+微调」流水线，成本更低效果优于直接调用通用大模型

  - 垂直领域效果验证可参考两层benchmark设计思路：先做基础规则/语法类验证集对齐认知，再做真实业务场景验证集保障业务效果

  - 低延迟业务（搜索实时补全、推荐实时触发）优先优化小参数量垂直专项模型，更容易达成实时响应要求且部署成本更低'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
通用代码LLM在训练数据稀缺的低资源编程语言上表现极差，动态语言Pharo的官方IDE当前仅支持单token补全，开发者工具体验落后。
### 方法关键点
1. 端到端优化流水线：结合Pharo专属数据 curation、开源代码LLM继续预训练、垂直任务微调三个环节
2. 两层基准测试集：分别用于验证模型对Pharo语法的掌握程度、真实GitHub仓库掩码代码的补全准确率
### 关键结果
Pharo专项定制模型效果大幅优于原基础checkpoint，在Pharo代码补全任务上准确率超过参数量远大于自身的通用代码大模型，模型体积足够小可支持IDE实时交互。
