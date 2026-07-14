---
title: The Effect of Multi-Lingual and Keyword Adversarial Injection on LLM Relevance
  Judgment
title_zh: 多语言与关键词对抗注入对LLM相关性判断的影响
authors:
- Nguyen Khoi Vo
- Duy Duong Tuong
- Oleg Zendel
- Mark Sanderson
affiliations:
- RMIT University
arxiv_id: '2607.10080'
url: https://arxiv.org/abs/2607.10080
pdf_url: https://arxiv.org/pdf/2607.10080
published: '2026-07-11'
collected: '2026-07-14'
category: Eval
direction: LLM评估 · 对抗注入鲁棒性
tags:
- LLM-as-a-judge
- Adversarial Injection
- Multilingual
- Relevance Judgment
- Prompt Defense
one_liner: 验证多语言内容/指令对抗注入可绕过现有防御，大幅抬升LLM相关性判断假阳率
practical_value: '- 电商/搜索业务做LLM自动相关性标注时，需新增多语言关键词注入检测模块，防范黑帽SEO用小语种关键词堆砌抬升非相关内容的排序

  - 选用LLM-as-a-judge做算法效果评估时，优先使用增强版PromptArmor类防御，明确加入query变体、多语言关键词的检测规则，降低评估偏差

  - 跨语种业务不要依赖单一语种的prompt注入过滤规则，需覆盖所有目标语种的关键词变体、语义干扰内容的检测逻辑'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM已大规模替代人工做搜索、推荐、广告的相关性自动标注，现有对抗注入研究仅聚焦单语种指令攻击，对多语言内容类注入（类似黑帽SEO的关键词堆砌、语义干扰等手段）的攻击有效性、防御效果缺乏系统性验证，直接影响排序公平性和评估结果可信度，亟需明确风险边界。
### 方法关键点
- 覆盖两类攻击范式：指令类注入、内容类注入（含原query关键词、query语义变体、无关干扰内容），测试8种不同资源等级、书写体系的语言
- 验证对象为两个主流开源LLM：GPT-OSS-20B、Qwen3-32B，适配UMBRELA、Criteria-Based两种工业界常用的相关性判断prompt框架
- 对比三类防御的效果：基础关键词规则过滤、PromptArmor原生版本、新增query注入检测的增强版PromptArmor
### 关键实验结果
- 数据集采用TREC-DL 2022标准检索基准，以人工标注为真值，核心指标为假阳率（FP，相关性高估比例）、假阴率（FN，相关性低估比例）
- 无攻击基线：GPT-OSS FP 19%、FN 5%；Qwen3 FP 23%、FN 3%
- 无防御场景下，多语言注入最高可将Qwen3的FP抬升至69%，所有语种的攻击均能稳定抬升FP 4~46个百分点
- PromptArmor可将指令类攻击的FP降至接近基线，但对内容类注入仅能抵消30%左右的攻击效果，query变体、语义干扰类攻击仍能将Qwen3的FP抬升至35%，且可绕过增强版防御
### 核心结论
多语言内容类对抗注入是LLM-as-a-judge未被覆盖的核心攻击面，单一通用防御无法完全抵御，需结合业务场景设计多层检测机制
