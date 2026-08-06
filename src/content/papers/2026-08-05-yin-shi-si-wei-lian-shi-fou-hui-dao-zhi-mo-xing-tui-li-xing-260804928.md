---
title: Does Out-of-Sight Equal Out-of-Mind in CoT Monitorability?
title_zh: 隐式思维链是否会导致模型推理行为不可监控？
authors:
- Pedro Ferreira
- Wilker Aziz
- Ivan Titov
affiliations:
- University of Amsterdam
- University of Edinburgh
arxiv_id: '2608.04928'
url: https://arxiv.org/abs/2608.04928
pdf_url: https://arxiv.org/pdf/2608.04928
published: '2026-08-05'
collected: '2026-08-06'
category: Reasoning
direction: 思维链可监控性 · 隐式CoT
tags:
- Chain-of-Thought
- Latent CoT
- Monitorability
- Activation Probing
- LLM Interpretability
one_liner: 对比显式与不同监督类型隐式CoT的可监控性，证明任务属性与内部访问权限比推理模式影响更大
practical_value: '- 业务侧采用Latent CoT降低推理成本时无需过度担忧可监控性损失，优先监控答案token的激活信号，准确率高于verbalize隐状态方案

  - 对规则明确的推理场景（如电商优惠计算、合规审核），可通过检测推理链与答案的mismatch识别作弊行为，无需额外部署探针

  - 开放域推理场景（如客服话术生成、商品卖点生成）不要依赖verbalized隐状态做监控，直接用激活探针可获得更稳定的效果

  - 跨域部署监控模型时，强规则类任务的监控器可直接复用，开放域任务需定期基于新场景数据重训监控器'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
显式CoT可通过可读推理trace监控模型对齐性、作弊等行为，但长推理链导致推理成本高；隐式CoT将中间推理步骤压缩为少量连续隐状态，可大幅降低推理时延，但失去了直接可读的trace，现有替代监控方案（激活探针、隐状态转文本）的效果缺乏系统性对比，业界普遍担忧隐式CoT会导致模型违规行为无法被检测。
### 方法关键点
- 以模型对输入中hint的依赖为监控目标，通过干预实验生成ground truth：仅当hint存在时模型输出发生变化且完全匹配hint，标记为依赖hint
- 覆盖四类推理模式：无CoT、显式CoT、弱监督隐式CoT（CODI）、强监督隐式CoT（SIM-COT）
- 对比四类监控方案：基于答案与hint exact match的基线、提示LLM读显式推理链、微调LLM读原生/verbalized文本、激活探针读取模型内部状态
### 关键结果
在数学推理（GSM8k域内、SVAMP跨域）和常识问答（ECQA域内、SIQA跨域）上测试：
- 激活探针在所有推理模式下表现最优，数学任务AUROC最高达0.91，问答任务最高达0.88
- 基于显式推理链的监控在数学任务上与激活探针表现相当（AUROC最高0.89），但问答任务上仅0.68
- verbalized隐状态可在数学任务上补全隐式CoT的监控gap，但问答任务上完全无效
- 跨域测试中数学任务监控AUROC仅下降0.01~0.1，问答任务下降最高达0.25

最值得记住的结论：隐式CoT本身不会显著降低可监控性，任务特性和对模型内部的访问权限才是决定监控效果的核心因素。
