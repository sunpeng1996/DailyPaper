---
title: 'StudentBench: AI and human tutoring yield equivalent GRE learning gains'
title_zh: 《StudentBench：AI辅导GRE学习效果与人类教师相当》
authors:
- Curtis Northcutt
- Inaara Hasmani
- Kevin Feng
- Trevor Khangi
- Andreas Plesner
- Jonas Mueller
arxiv_id: '2609.28470'
url: https://arxiv.org/abs/2609.28470
pdf_url: https://arxiv.org/pdf/2609.28470
published: '2026-09-22'
collected: '2026-09-26'
category: Eval
direction: LLM 教学效果评估基准构建
tags:
- LLM
- Evaluation Benchmark
- Tutoring Agent
- Cost Efficiency
- Human-AI Comparison
one_liner: 推出AI教学效果评估基准StudentBench，验证AI GRE辅导效果等价人类且成本低918倍
practical_value: '- 可复用「大规模随机分组对照+双盲配对评分」的评估范式，用于验证电商导购/客服LLM Agent替代人工的效果等价性

  - 单位效果成本的量化对比方法可直接迁移，辅助业务决策是否将人工服务切换为AI Agent方案

  - AI回复时延与用户互动量、任务完成率正相关的结论，可用于指导电商咨询Agent的工程优化，优先降低回复时延'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM研发多聚焦模型能力升级，缺乏可大规模量化AI服务与人类服务效果差异的统一评估框架，AI辅导能否达到人类教师的教学效果尚无严谨实证结论。
### 方法关键点
1. 推出StudentBench评估套件与公开平台，支持百万级学生-AI交互数据采集
2. 两组对照实验：2383名GRE考生分AI辅导、人类辅导、无辅导三组对比学习收益；专家教师完成2028次AI/人类教案、习题的配对评分
### 关键结果
- AI辅导的GRE学习收益与人类专家辅导统计等价（p=0.015），7个GRE考点中5个AI平均表现优于人类
- 最优AI tutor效果等价人类的前提下，单位学习收益成本仅为人类的1/918
- 数学类辅导中AI回复越快，学生互动量、习题正确率、学习收益越高（所有p<0.002）
