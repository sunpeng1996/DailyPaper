---
title: 'PhysClaw-0: A Symbiotic Agentic System for Robot Autonomy via Language Corrections'
title_zh: PhysClaw-0：基于语言纠错的人机共生自主机器人智能体系统
authors:
- Boyuan Wang
- Zhenyuan Zhang
- Zhiqin Yang
- Peijun Gu
- Shuya Wang
- Xiaofeng Wang
- Xianghui Ze
- Yifan Chang
- Guosheng Zhao
- Jiangnan Shao
affiliations:
- GigaAI
- 中国科学院大学
- 香港科技大学
- 利兹大学
- 康奈尔大学
arxiv_id: '2607.14047'
url: https://arxiv.org/abs/2607.14047
pdf_url: https://arxiv.org/pdf/2607.14047
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent · 人机共生语言纠错系统
tags:
- Agentic System
- Human-Robot Interaction
- Corrective Memory
- Language Feedback
- Robotic Data Collection
one_liner: 提出带持久化纠错记忆的人机共生数据采集系统，人工工时仅为全遥操作的16%
practical_value: '- 可复用「验证门控决策+重试预算阈值」架构，在推荐bad case拦截、广告创意合规校验、AB实验效果核验等场景中，仅当失败次数超过阈值才触发人工介入，大幅降低运营人力成本

  - 可借鉴Corrective Memory设计，将运营/标注人员的自然语言反馈转为结构化可复用规则，解决推荐bad case反复出现、同类问题重复人工干预的痛点

  - 可复用TpHM（有效产出/单位人工时长）指标框架，用于评估内容标注、bad case治理、用户反馈处理等人力密集型环节的投入产出比'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
VLA（视觉语言动作）模型性能高度依赖真实世界演示数据的规模与质量，现有数据采集方案要么需要全程人工遥操作成本极高，要么全自动化方案长期运行时长尾故障反复出现，单次纠错仅生效于当前任务，监管成本随采集时长线性上升，无法实现经验复用。

### 方法关键点
- 设计验证门控的采集-重置闭环，每个阶段（采集/重置）执行后由VLM判定结果，失败后自动重试，超过预设重试阈值才触发人工告警，明确划分自治与人工介入边界
- 搭建自然语言纠错通道与持久化Corrective Memory，由LLM解析器将操作者的自然语言纠错转为结构化规则（包括验证标准调整、执行策略修正等），存储后自动匹配后续所有同类场景，无需重复干预
- 采集的合规轨迹直接用于下游VLA模型微调，形成「采集-纠错-训练-部署」的数据飞轮，纠错规则同步作用于数据质量校验标准

### 关键结果
在桌面清理真实机器人测试集上：采集成功率与全人工遥操作持平（100%），人工工作时间仅为遥操作的16%，TpHM（每分钟人力产出有效轨迹数）达10.42，是遥操作的6倍；语言纠错将VLM验证准确率在4个测试场景中最高提升100%，单轮采集成功率从12.5%提升至47.5%，臂选场景从20%提升至50%；基于PhysClaw-0采集数据微调的VLA模型，部署成功率达80%，与全人工遥操作数据训练的模型性能持平。

### 核心结论
让人工干预的价值随使用次数递增而非一次性消耗，是大幅降低人机协作系统人力成本的核心路径。
