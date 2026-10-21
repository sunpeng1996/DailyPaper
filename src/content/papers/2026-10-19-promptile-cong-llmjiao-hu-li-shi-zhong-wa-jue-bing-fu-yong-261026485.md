---
title: 'Promptile: Recovering and Reusing Prompting Strategies from LLM Interaction
  Histories'
title_zh: Promptile：从LLM交互历史中挖掘并复用用户Prompt策略
authors:
- Qingyang Wan
- Chang Liu
- Zhoutong Ye
- Chengwen Zhang
- Yanru Qian
- Zhike Wang
- Jie Cai
- Chun Yu
- Yuanchun Shi
affiliations:
- 清华大学
- 剑桥大学
- 中国人民大学
- 南开大学
arxiv_id: '2610.26485'
url: https://arxiv.org/abs/2610.26485
pdf_url: https://arxiv.org/pdf/2610.26485
published: '2026-10-19'
collected: '2026-10-21'
category: LLM
direction: LLM交互 · Prompt策略挖掘复用
tags:
- LLM Prompting
- User Modeling
- Interaction History
- Preference Extraction
- Reusable Prompt
one_liner: 从用户LLM交互历史中提取模块化Prompt策略片段，支持检索组合降低重复Prompt输入成本
practical_value: '- 可复用Prompt片段拆解+检索组合的架构，优化电商用户与导购Agent交互体验：将用户常用的prompt约束（如商品推荐要按价位分层、标注适配场景）提取为可复用片段，减少用户重复输入成本

  - 可借鉴用户对Prompt片段的接受/修改/删除隐式反馈更新检索权重的机制，用于推荐系统用户偏好的动态迭代，无需用户显式标注

  - 四维度Prompt偏好分类法（Context/Instruction/Supporting Info/Output）可直接迁移到电商Agent prompt模板生成场景，标准化不同业务的prompt组件'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM个性化方案大多聚焦用户偏好建模、历史对话召回，用户长期积累的Prompt策略（如固定输出格式、角色设定、思考步骤要求）散落在不同对话中无法复用，用户遇到同类任务需重复输入相同约束，交互成本高，还容易遗漏过往验证有效的Prompt技巧。

### 方法关键点
- 通过用户研究定义四维度Prompt偏好分类法：Context（任务领域、上下文依赖）、Instruction（任务指令、角色、行为约束、流程要求）、Supporting Info（示例、背景知识、参考资料）、Output（格式、风格、长度要求），作为片段拆解的标准
- 框架分四大模块：①历史处理模块：双Agent从对话中提取经用户验证有效的Prompt片段，分类存入偏好库；②检索模块：新任务到来时按语义相似度从三个可复用维度各召回Top5片段，加权排序后做语义去重；③交互组装模块：支持用户拖拽、编辑、删除片段，自动润色为通顺Prompt；④反馈更新模块：根据用户对片段的操作调整检索权重，持续适配用户偏好

### 关键实验
基于WildChat长时序交互数据+16名用户的对照实验，对比开启全局记忆的ChatGPT baseline：①Prompt策略提取准确率91%，用户对分类准确性的7点Likert评分均值达6.4分；②用户手动输入字符量减少44%（51.38 vs 91.63），交互轮次降低30%（1.88 vs 2.69），任务挫败感显著下降，用户感知任务完成度提升19.6%

### 核心洞察
Prompt复用的核心不是照搬历史Prompt原文，而是把过往验证有效的策略拆解为可组合的模块化片段，让用户从「从零写Prompt」转向「编辑筛选偏好片段」，本质是把用户的交互努力从提交后的多轮纠错转移到提交前的可控组装，大幅降低整体交互挫败感
