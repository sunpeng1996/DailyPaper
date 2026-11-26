---
title: 'Loupe: Reinforcing Knowledge-Intensive Video Generation Agents'
title_zh: Loupe：面向知识密集型场景的视频生成Agent强化框架
authors:
- Kai Zeng
- Ruichuan An
- Zhen Fang
- Xi Fang
- Han Lyu
- Moran Li
- Yingchen Yu
- Yifan Dai
- Bohan Zeng
- Quanqing Xu
affiliations:
- DP Technology
- PKU
- USTC
- HUST
- Ant Group
arxiv_id: '2611.31895'
url: https://arxiv.org/abs/2611.31895
pdf_url: https://arxiv.org/pdf/2611.31895
published: '2026-11-23'
collected: '2026-11-26'
category: Agent
direction: Agent · 过程监督与信用分配
tags:
- Agent
- Process Supervision
- Credit Assignment
- Tool Use
- Video Generation
one_liner: 提出基于请求自定义评分规则的步骤级信用分配机制，训练搜索增强视频生成Agent，无需渲染即可完成RL优化
practical_value: '- 过程监督设计可直接迁移到电商广告/营销素材生成Agent：无需等待真实投放反馈，基于用户需求拆解的自定义评分规则（如卖点完整性、品牌合规性、活动时效准确性），即可给每步工具调用（素材搜索、活动规则查询、竞品信息检索）打分，实现RBC-SFT和RBC-GRPO训练，大幅降低训练成本

  - 步骤级信用分配trick可复用在所有多轮工具调用Agent训练中：SFT阶段按步骤质量加权对应token损失，RL阶段按同请求同交互轮次做奖励归一化，解决轨迹级奖励掩盖单步贡献的问题，适配电商导购Agent、搜索query改写Agent等场景

  - 知识密集型生成任务的评测体系可复用：先拆解任务的核心评估维度（如事实性、视觉一致性、时序合理性），再构造带明确评分规则的测试集，可直接用于电商商品短视频生成、营销文案生成的效果评估体系建设'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
知识密集型视频生成易出现实体幻觉、外观错配、时序错误，现有搜索增强方案依赖人工设计策略，泛化性差；传统训练范式要么SFT对所有决策token一视同仁，要么RL依赖最终视频反馈，成本高且轨迹级奖励无法准确分配单步贡献，同时缺乏针对搜索增强视频生成的专用评测基准。

### 方法关键点
- 设计Loupe Agent，遵循ReAct交互逻辑调用文本搜索、图片搜索、网页浏览工具，自动识别请求知识缺口，多轮检索验证证据后输出带参考图的时序化视频prompt
- 提出Rubric-Based Credit（RBC）机制，从用户请求拆解出无标准答案的评分规则（覆盖事实、视觉、时序三类要求），用大模型裁判给每轮Agent决策打分，无需渲染视频
- 训练范式：RBC-SFT按步骤得分加权对应token损失，聚焦高质量决策；RBC-GRPO融合步骤级奖励与最终规划奖励，按同请求同交互轮次做奖励归一化，规避轨迹级奖励偏差
- 构建Search-VBench评测集，含7类共150条知识密集型prompt、339张参考图、566条评分规则，从4个维度评估生成效果

### 关键结果
适配3个主流视频生成基座实现全维度提升，MiniMax-H3总得分从32.80升至70.67，较未训练的搜索工作流高21.27分，人工偏好率达82.33%；完整RBC训练流程比标准SFT+轨迹级GRPO高5.27分；在KIVI-Bench上事实精度提升9个百分点。

> 核心结论：用户请求本身隐含验证标准，即使无标准答案，也可基于请求拆解的评分规则实现多轮Agent的低成本过程监督。
