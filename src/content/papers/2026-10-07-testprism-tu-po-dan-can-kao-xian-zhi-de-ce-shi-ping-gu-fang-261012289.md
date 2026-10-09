---
title: 'TestPrism: Rethinking Test Evaluation Beyond a Single Reference'
title_zh: TestPrism：突破单参考限制的测试评估方法与基准
authors:
- Han Li
- Lingxiang Hu
- Jiacheng Huang
- Ziqian Jiang
- Jingkai Luo
- Wei Gao
- Yunfan Tan
- Zun Wang
- Jiaheng Liu
affiliations:
- Nanjing University
- Hong Kong Polytechnic University
- Tencent
arxiv_id: '2610.12289'
url: https://arxiv.org/abs/2610.12289
pdf_url: https://arxiv.org/pdf/2610.12289
published: '2026-10-07'
collected: '2026-10-09'
category: Eval
direction: LLM编码Agent 测试评估基准构建
tags:
- Test Evaluation
- LLM Agent
- Benchmark
- Test Generation
- Code Agent
one_liner: 提出多参考测试评估基准TestPrism与优化框架TestHelix，解决单参考评估高估测试质量问题
practical_value: '- 评估业务自动化Agent/代码生成Agent输出时，可复用多参考校验思路，避免单参考漏判多种合法实现，降低评估误判率

  - 可借鉴Joint Success Function的设计逻辑，为业务Agent输出制定「漏判+误判双向校验」的评估标准，提升评估严谨性

  - TestHelix的同行交叉校验+递归自优化思路可迁移到推荐策略/运营规则自动生成场景，提升输出结果鲁棒性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM编码Agent的测试生成评估普遍采用单参考方案，忽略同需求下多种合法实现的可能性，严重高估测试质量，缺乏公平全面的评估基准。
### 方法关键点
1. 构建TestPrism基准，覆盖17个来源的300个测试任务，配套3000个候选实现（合法/非法各占50%）；
2. 提出核心评估指标Joint Success Function，要求生成的测试同时满足「初始程序状态不通过、所有合法实现通过、所有非法实现不通过」三个条件；
3. 推出TestHelix优化框架，融合测试-修复对异构合成、同行交叉校验、递归自优化（RSI）能力。
### 关键结果
14种基线编码Agent配置的单参考评估成功率达59.67%，但Joint Success Function仅为28.00%；TestHelix在两类模型上可将Joint Success Function相对原生方案提升8.67~9.00个百分点。
