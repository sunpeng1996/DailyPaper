---
title: 'LifeVal: Evaluating AI Model Performance on Personalized Agentic Consumer
  Tasks'
title_zh: LifeVal：面向个性化智能体消费类任务的AI模型性能评估基准
authors:
- Jenny Yang
- Elizabeth Proehl
- Anjan Bharadwaj
- Emily Fan
- Charlotte Cole
- James Kim
- Noam Brown
- Phoebe Thacker
- Amelia Glaese
- Tejal Patwardhan
affiliations:
- OpenAI
arxiv_id: '2611.06687'
url: https://arxiv.org/abs/2611.06687
pdf_url: https://arxiv.org/pdf/2611.06687
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: Agent 个性化消费任务能力评估
tags:
- Agent
- Benchmark
- Personalization
- LLM
- Evaluation
one_liner: OpenAI推出按消费者付费意愿加权的个性化智能体消费类任务评估基准
practical_value: '- 构建电商/生活服务类个性化Agent的评估体系时，可复用「用户付费意愿加权」的任务筛选逻辑，替代传统时间花费加权，对齐用户真实需求优先级，避免在低价值任务上浪费优化资源。

  - 个性化任务的批量评估可采用「任务专家制定rubric + 大模型自动评分」的方案，论文验证该方案与人工评分的皮尔逊相关系数达0.864，准确率足够，可大幅降低评估人力成本。

  - 开发电商导购、个人助理类Agent时，建议将用户核心偏好从长对话历史中单独抽取为结构化上下文，避免模型从长对话提取信息的低成功率（仅33.3%），可直接提升个性化任务完成率。

  - 评估Agent能力时需新增环境作弊检测环节，避免模型利用测试环境的内部API漏洞作弊，保证实验室评估结果与线上真实表现对齐。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有AI Agent评估多聚焦工作场景或通用学术任务，常以用户时间花费加权排序任务，无法准确衡量消费类个性化长周期任务的真实价值，也无法覆盖用户尚未主动提出的高价值潜在需求，急需对齐用户真实付费意愿的消费类Agent评估体系。
### 方法关键点
- 任务筛选：结合3800+美国人口代表性样本的WTP（付费意愿）调研、ATUS时间使用调查、MTUS跨国时间使用数据，筛选148类年总WTP达1.7万亿美元的高价值消费任务，覆盖理财、搬家、求职、育儿等场景。
- 任务构建：招募有1年以上真实任务经验的创作者，基于其脱敏ChatGPT对话历史、记忆、参考文件构建个性化任务，每类任务配套专属评分rubric、强化学习执行环境、初始状态，经至少3轮人工+模型质量校验后入库。
- 评分机制：采用双自动评分器，主评分器基于任务上下文、rubric、模型输出、环境状态变化打分；hack评分器检测是否调用环境内部API作弊，作弊任务得0分。
### 关键实验
基于169个验证任务测试GPT-5.2到GPT-6 Astra的表现：① 模型从长对话历史提取关键偏好的成功率仅33.3%，远低于从结构化额外上下文提取的55.8%；② GPT-5.6自动评分与人工评分的皮尔逊相关系数达0.864，平均分偏差小于1%。
### 关键结论
对消费类个性化Agent而言，用户在任务上的时间花费是价值的弱代理指标，付费意愿才是更准确的优先级锚点。
