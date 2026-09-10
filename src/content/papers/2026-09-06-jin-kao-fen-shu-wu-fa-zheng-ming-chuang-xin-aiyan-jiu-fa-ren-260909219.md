---
title: 'Scores Alone Do Not Prove Discovery: The Discovery Certification Protocol
  for Auditing AI Research Agents'
title_zh: 仅靠分数无法证明创新：AI研究Agent的发现认证协议
authors:
- Jingjie Ning
- Shanshan Zhong
- Xiaochuan Li
- Ji Zeng
affiliations:
- Carnegie Mellon University
arxiv_id: '2609.09219'
url: https://arxiv.org/abs/2609.09219
pdf_url: https://arxiv.org/pdf/2609.09219
published: '2026-09-06'
collected: '2026-09-10'
category: Agent
direction: AI研究Agent · 成果审计评估
tags:
- AI Research Agent
- Audit Protocol
- Evaluation
- Causal Inference
- Discovery Validation
one_liner: 提出三关卡可执行审计协议DCP，验证AI研究Agent成果的原创性与反馈价值
practical_value: '- 做业务Agent（如选品Agent、文案生成Agent）效果验证时，可复用DCP三关卡思路：先验证业务收益，再做信息边界隔离的复现测试，最后量化反馈模块的真实贡献，避免把训练数据泄露、随机试错得到的好结果当成Agent本身的能力

  - 评估推荐/广告系统的新算法增益时，可参考Gate2的recovery测试设计，控制相同的特征、算力、数据边界，验证新算法是否真的有不可替代的价值，避免调参、数据泄露带来的虚假提升

  - 做Agent迭代优化时，可复用Gate3的随机配对对照方案，用中性反馈做baseline，精准量化反馈链路的真实因果增益，避免随机波动、初始信息的干扰

  - 做业务效果校验时，可参考DCP的预注册机制，提前冻结评估规则、baseline、阈值，避免后验改规则带来的效果虚高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前AI研究Agent已可自动生成算法、模型、实验方案，但传统仅看最终性能分数的评估方式，无法区分成果是真实创新发现，还是靠记忆已有内容、数据泄露、随机试错刚好获得，也无法量化Agent自适应反馈环节的真实价值，缺乏可复现、可量化的统一审计标准。
### 方法关键点
- 三关卡审计架构：Gate1密封评估验证成果相对baseline的显著有用增益；Gate2给匹配挑战者Agent完全相同的初始信息、公开内容、资源预算，仅 withholding目标Agent的实验历史，测试能否复现同等性能，零复现且复现概率上界低于阈值即可通过Core认证；可选Gate3从共享checkpoint出发，分别给Agent真实反馈和中性反馈，量化真实反馈的因果增益，通过空校准后获得Evidence认证。
- 可执行规则设计：用数值阈值定义复现，所有合法方法均可参与挑战，避免人工判断主观性；所有评估规则、阈值、资源预算提前预注册，避免后验调整。
- 确定性可复现：所有审计证据支持离线无LLM验证器重放，决策完全透明可追溯。
### 关键实验
在SQLite优化、虚拟催化剂控制两个任务上测试，分别采用DeepSeek-v4-flash、DeepSeek-v4-pro作为被审计Agent：Gate2各执行96次挑战者测试，均零复现，复现概率上界≤0.0468；Gate3各30组配对测试，真实反馈组全部复现成果，中性反馈组零复现，同时60组空校准测试全部通过，两个任务均拿到Core+Evidence认证。
### 核心结论
AI系统的高性能不等于真的产生了新的发现或能力，必须在严格控制信息边界和对照的前提下，才能验证其真实贡献。
