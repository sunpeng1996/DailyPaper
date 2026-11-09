---
title: 'Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making'
title_zh: 多智能体LLM决策中的幻影共识现象测量与基准构建
authors:
- Disha Sheshanarayana
- Rajat Subhra Pal
- Manjira Sinha
- Tirthankar Dasgupta
affiliations:
- Manipal University Jaipur
- TCS Research
arxiv_id: '2611.08971'
url: https://arxiv.org/abs/2611.08971
pdf_url: https://arxiv.org/pdf/2611.08971
published: '2026-11-06'
collected: '2026-11-09'
category: MultiAgent
direction: 多智体决策 · 社会推理失效测量
tags:
- MultiAgent
- SocialReasoning
- LLM
- Benchmark
- CollectiveDecisionMaking
one_liner: 提出PHANTOM-BENCH基准，测量多智能体LLM错误推断同伴判断引发的群体决策失效
practical_value: '- 多智能体协作做商品选品/广告审核/内容治理场景，可先强制所有Agent输出独立私有判断再公开讨论，该方案对部分模型的决策失效修复率可达99.6%

  - 搭建多智能体决策pipeline时，可参考论文的5种信念上下文条件做对齐验证，区分Agent决策偏移是源于直接从众还是错误推断群体隐含态度，针对性优化prompt

  - 小参数开源LLM做Agent应用时需额外加入防从众校验逻辑：Qwen-2.5-7B这类小模型受模糊信号影响最大，决策准确率最高下降47.8个百分点，集体失败率达47.3%'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多智能体LLM系统常依赖群体投票/共识提升决策质量，但现有研究多关注显性从众行为，忽略模糊社交信号下Agent错误推断同伴私有判断、进而产生无实际私有支持的虚假共识（幻影共识）的问题，这类失效会导致原本正确的群体私有判断最终输出错误公共决策，是多智能体落地必须解决的隐性风险。

### 方法关键点
- 提出PHANTOM-BENCH基准，覆盖金融合规、内容审核、招聘公平等5个决策领域共480个三分类决策场景，每个场景定义事实支撑的金标准私有决策、以及模糊信号可能引导的错误幻影目标
- 设计5种信念上下文对照条件：私有判断（无群体信息）、观察公开模糊信号、私有判断透明公开、中性公开文本、显式投票信号，分离直接从众、文本干扰、错误推断群体信念等不同失效机制
- 定义PPG（私有-公共准确率差）、CRFR（群体理性失效率）、TRR（透明恢复率）等多维度指标，同时采集Agent对群体私有判断的认知，直接度量二阶信念误差

### 关键实验
在9款闭源/开源LLM上测试，无公开信号时私有判断准确率最高达80.1%，暴露模糊公开信号后，Qwen-2.5-7B准确率下降47.8个百分点，群体理性失效率达47.3%，其中39.4%的失效完全对齐幻影目标；公开所有Agent的私有判断后，多数模型的决策失效恢复率超过90%，最高达99.6%。

### 核心结论
多智能体LLM的最终共识可信度不仅取决于一致性比例，更要验证该共识是否与各Agent的独立私有判断对齐，而非源于对模糊信号的错误推断。
