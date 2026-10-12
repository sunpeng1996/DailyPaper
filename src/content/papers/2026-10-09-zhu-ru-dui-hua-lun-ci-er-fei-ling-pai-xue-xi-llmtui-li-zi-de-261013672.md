---
title: 'Inject a Turn, Not a Token: Learning Where to Redirect LLM Reasoning for Self-Correction'
title_zh: 注入对话轮次而非令牌：学习LLM推理自修正的干预位置
authors:
- Jiwon Jeon
- Myungsik Cho
- Jeonghye Kim
- Youngchul Sung
affiliations:
- Korea Advanced Institute of Science and Technology (KAIST)
arxiv_id: '2610.13672'
url: https://arxiv.org/abs/2610.13672
pdf_url: https://arxiv.org/pdf/2610.13672
published: '2026-10-09'
collected: '2026-10-12'
category: Reasoning
direction: LLM推理自修正 · 轻量无微调干预
tags:
- Self-Correction
- Reasoning
- LLM
- Lightweight Intervention
- Multi-Turn Prompting
one_liner: 无需微调LLM，通过轻量头部学习干预位置，以新用户轮次注入指令实现高效推理自修正
practical_value: '- 做Agent/生成式文案/query改写的自修正时，不要内联插入修正指令，改为新增独立用户轮次注入，可大幅提升修正成功率

  - 无需微调推理大模型，仅用100K级小MLP头+冻结小编码器即可实现干预位置学习，落地成本极低，适合快速上线

  - 66K参数的轻量gate仅需少量标注数据即可筛选bad case，可复用在各类生成式业务的错误样本过滤场景

  - 该框架可直接叠加在现有GRPO优化、自修正流程之上，无需重训即可获得额外效果增益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM自修正方案普遍存在成本高、效果差的问题：要么需要微调大模型或训练LLM级别的校验器，依赖大量step级标注；要么内联注入的修正指令容易被模型吸收为现有推理的一部分，无法有效转向错误路径。同时LLM自回归推理的特性决定了单步错误会导致后续全链路失效，亟需低成本的干预方案。
### 方法关键点
1. 仅训练两个超轻量MLP头：130K参数的位置选择头（搭载冻结的Qwen3-0.6B编码器）用于选择推理链的切分点，66K参数的gate头用于筛选需要修正的失败推理样本，全程不微调推理LLM；
2. 修正指令采用独立用户轮次注入，而非内联插入推理文本，通过对话结构触发模型切换推理路径；
3. 用GRPO变体训练位置头，仅用最终答案正确性作为奖励信号，无需step级标注，切分点限制在段落边界（\n\n）降低计算开销。
### 关键结果
在4款参数覆盖4B~32B的推理LLM、6个数学基准测试集上，UPTURN@16平均准确率比32次采样的Base@32高18.2pp，比同预算下最强基线Reflexion高16.2pp；跨模型、跨领域（迁移到GPQA-Diamond科学题）无需重训仅掉点<3pp，还可在GRPO、现有自修正方法基础上额外提升4~12pp准确率。
### 核心结论
当LLM已具备解决问题的基础能力时，仅需在合适位置插入1个新用户轮次的修正指令，即可低成本恢复正确推理路径，无需微调大模型
