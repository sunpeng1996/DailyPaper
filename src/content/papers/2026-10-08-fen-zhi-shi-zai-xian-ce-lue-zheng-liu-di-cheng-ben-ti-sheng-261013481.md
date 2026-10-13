---
title: Branching On-Policy Distillation
title_zh: 分支式在线策略蒸馏：低成本提升小模型推理与Agent性能
authors:
- Dongyang Chen
- Shudong Liu
- Shubo Li
- Duoxun Tang
- Jinwei Liang
- Zehuan Wu
- Lewei Lu
affiliations:
- Tsinghua University
- Peking University
- SenseTime Research
arxiv_id: '2610.13481'
url: https://arxiv.org/abs/2610.13481
pdf_url: https://arxiv.org/pdf/2610.13481
published: '2026-10-08'
collected: '2026-10-13'
category: Training
direction: LLM蒸馏与Agent训练优化
tags:
- On-policy Distillation
- Knowledge Distillation
- LLM Agent
- Policy Optimization
- Mathematical Reasoning
one_liner: 通过决策点分支采样+协议边界修复，大幅提升在线策略蒸馏的效率与效果
practical_value: '- 做电商导购Agent/搜索Query理解小模型蒸馏时，可复用分支采样策略：在学生输出不确定、与大教师模型输出分歧大的决策点重采样后缀，复用前缀减少30%左右的生成token成本，同时覆盖更多错误路径提升蒸馏效果

  - 解决Agent输出重复、格式错误问题时，可直接复用PBR（协议边界修复）方法：针对业务定义的合法输出规则（如商品查询必须以<search>标签开头、回答结束必须输出EOS）设置正负约束的辅助损失，比通用重复惩罚效果提升明显

  - 小模型落地多轮交互任务（如智能客服、商品推荐助手）时，可优先选择BranchOPD替代普通OPD，相同token预算下ALFWorld任务成功率提升13.8个百分点，且无需额外任务reward，适配无明确业务反馈的冷启动蒸馏场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有On-policy Distillation（OPD）仅在学生生成的单条轨迹上做教师监督，每个决策点仅探索一条路径，监督覆盖范围有限；如果采样多条独立轨迹又会重复生成相同前缀，浪费计算资源，同时OPD普遍存在学生输出重复、长度膨胀、违反输出协议的问题，导致蒸馏效果受限。

### 方法关键点
- 分支采样策略：先生成主轨迹，用学生输出熵（不确定性）、师生输出分歧两个信号打分选择分叉点，从分叉点重采样多个后缀，共享前缀仅计算一次损失，大幅降低token开销
- 分叉点选择规则：数学任务直接选token级分叉点，Agent任务先选高得分轮次再在轮内选分叉点，默认3个分叉点每个采样2个后缀，共7条轨迹
- 协议边界修复（PBR）：针对业务定义的输出协议事件（如数学题输出答案后需终止、Agent回答不能出现多余闭合标签）设置正负约束的辅助损失，直接修正不符合规则的输出

### 关键结果
实验覆盖数学推理（DAPO-Math-17K、MATH-500、AIME 2024/2025）、Agent任务（ALFWorld、WebShop、Search-QA），对比Vanilla OPD、Multi-Rollout OPD（n=7）等基线：
- 数学任务avg@16准确率比Vanilla OPD高18.55个百分点，比Multi-Rollout OPD（n=7）高5.28个百分点
- ALFWorld任务平均成功率比Vanilla OPD高13.8个百分点，比7条独立轨迹采样节省19%的学生生成token，WebShop场景节省31%token
- PBR单独使用可将Vanilla OPD数学准确率提升13.12个百分点，远优于通用重复惩罚方案

OPD的效果不仅取决于教师的监督信号，更取决于学生能探索到多少自己的错误历史并获得反馈。
