---
title: Last Translation Benchmark
title_zh: Last Translation Benchmark 机器翻译极限评测基准
authors:
- Vilém Zouhar
- Niyati Bafna
- Mukund Choudhary
- Maike Züfle
- Sara Rajaee
- Pinzhen Chen
- Jannis Vamvas
- Sara Papi
- Ona de Gibert
- Bhavitvya Malik
affiliations:
- ETH
- JHU
- MBZUAI
- KIT
- UvA
arxiv_id: '2609.04173'
url: https://arxiv.org/abs/2609.04173
pdf_url: https://arxiv.org/pdf/2609.04173
published: '2026-09-02'
collected: '2026-09-06'
category: Eval
direction: 大模型评测 · 机器翻译基准构建
tags:
- Benchmark
- Machine Translation
- Evaluation
- LLM Evaluation
- Test Dataset
one_liner: 发布由可攻破主流翻译模型的难例组成的动态基准LTB，配套带手动校验规则的可落地评估方法
practical_value: '- 跨境电商多语言翻译场景可直接引入LTB难例集做前置压力测试，提前识别小语种、专业术语翻译的漏判问题

  - 搭建LLM生成类任务（商品文案、营销话术生成）评测体系时，可复用「难例+对应校验规则」的思路，避免reward hacking、评测饱和问题

  - 业务侧自定义评测集可参考LTB的开源共建、动态迭代模式，持续收录模型bad case倒逼模型迭代'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
当前机器翻译领域标准基准已接近饱和，自动评测指标不可靠、易被reward hacking，输出评估结果无落地指导价值；人工黄金评测也存在可复现性差、客观性不足、难以规模化的问题，无法客观追踪模型真实进展、定位优化方向。
### 方法关键点
1. 构建LTB基准，所有样本均为经过同行评审、可攻破当前主流翻译模型的人类创作多模态内容（文本、图像、音频、视频）
2. 每个样本配套手动编写的校验规则，明确标注对应具体失败case，实现可靠、可落地的自动化评估
3. 采用动态开源共建模式，持续接受社区贡献更新版本
### 关键结果
当前最新版本为LTBv1，收录2026年9月1日前的所有有效贡献，后续将随新数据收集持续迭代发布新版本
