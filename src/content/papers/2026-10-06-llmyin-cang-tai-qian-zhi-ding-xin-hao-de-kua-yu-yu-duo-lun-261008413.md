---
title: 'Knowing When Not to Answer: Cross-Domain and Multi-Turn Generalization of
  Latent Underspecification Signals'
title_zh: LLM隐藏态欠指定信号的跨域与多轮对话泛化性研究
authors:
- Jerzy Kamiński
- Ilya Galyukshev
- Artem Kuznetsov
- Danil Fedorov
- Kirill Redko
- Sergey Chuprin
- Aidar Shumbalov
- Stanislav Chumakov
- Anna Kalyuzhnaya
affiliations:
- ITMO University
arxiv_id: '2610.08413'
url: https://arxiv.org/abs/2610.08413
pdf_url: https://arxiv.org/pdf/2610.08413
published: '2026-10-06'
collected: '2026-10-07'
category: LLM
direction: LLM隐态探针 · 可回答性检测
tags:
- Probing
- Unanswerability Detection
- Hidden State
- Cross-domain Transfer
- Multi-turn Dialogue
one_liner: 验证LLM可回答性隐态探针的跨域/跨结构泛化边界，实测部署收益低于Prompt基线
practical_value: '- 做Agent多轮澄清触发时，可复用同欠指定原因下的跨域探针训练方案：比如电商咨询缺参数（尺码、地址）这类同属「信息缺失」的场景，无需每个子场景单独标注数据，降低标注成本

  - 不要盲目迷信隐态探针的端到端收益：实测其澄清触发精度比随机高30%+，但整体效果不如RECAP类对话总结Prompt，优先测试低成本Prompt方案再考虑探针落地

  - 单轮可回答性探针无法直接迁移到多轮对话，若要做多轮欠指定检测，要么用多轮对话数据单独训练探针，要么直接用TF-IDF类文本分类基线，效果相当且工程成本更低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有研究证明LLM隐藏态可线性解码可回答性，用于抑制幻觉，但不清楚不同欠指定原因（问题缺信息、上下文缺信息、认识论不可知）的表征是否通用，也未验证多轮对话下的迁移能力，若信号通用可实现零微调的生成门控，避免模型在信息不足时强行回答。

### 方法关键点
- 探针方案：采用L2正则化逻辑回归拟合6类开源LLM的最后prompt token隐态，无模型微调，跨域/跨结构测试时探针完全冻结
- 数据集：覆盖3类欠指定原因的6个单轮数据集，以及自建的423条、1661个turn标注的多轮对话基准
- 评估框架：搭建模拟用户回答澄清问题的测试管线，对比探针门控、vanilla生成、Prompt引导、RECAP总结等基线

### 关键结果
- 同欠指定原因下探针跨域迁移AUROC达0.77~0.97（数学题场景）、0.77~0.90（抽取式QA场景），跨欠指定原因的迁移效果不稳定
- 单轮探针零-shot迁移多轮完全失效，多轮单独训练的探针效果与TF-IDF文本分类基线相当
- 探针门控的多轮澄清触发精度达0.74~0.88，比随机门控高20%+，但端到端任务成功率比RECAP基线低最多0.144，仅比oracle门控低0.08，差距主要在模型对澄清信息的利用而非检测

**最值得记住的一句话**：可回答性隐态探针的检测精度已接近理论上限，但端到端落地收益远低于低成本Prompt工程，优先优化对话交互策略而非隐态检测
