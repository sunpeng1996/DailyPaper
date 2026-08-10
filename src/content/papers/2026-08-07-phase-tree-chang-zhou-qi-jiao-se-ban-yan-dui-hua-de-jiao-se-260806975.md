---
title: 'PHASE-Tree: Modeling Character-State Evolution in Long-Horizon Role-Playing
  Dialogue'
title_zh: PHASE-Tree：长周期角色扮演对话的角色状态演化建模
authors:
- Bo Tang
- Jianan Yang
- Junyi Zhu
- Yiquan Wu
- Rui Zhao
- Zhengyu Yang
- Yang Zhang
- Feiyu Xiong
- Zhiyu Li
- Jiajun Shen
affiliations:
- MemTensor (Shanghai) Technology
- KU Leuven
- Zhejiang University
- University of Chinese Academy of Sciences
- The Hong Kong Polytechnic University
arxiv_id: '2608.06975'
url: https://arxiv.org/abs/2608.06975
pdf_url: https://arxiv.org/pdf/2608.06975
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agent 角色扮演对话状态演化
tags:
- Role-Playing
- Long-Horizon Dialogue
- Persona Modeling
- LoRA
- LLM Agent
one_liner: 提出多时间尺度角色状态树与长周期角色演化评测基准，解决角色扮演对话的状态过时问题
practical_value: '- 做电商智能客服、虚拟导购等长期交互Agent时，可复用分层状态设计：固定身份根（品牌/人设）+慢更长期属性（用户标签/长期偏好）+快更会话属性（当前需求/情绪），避免静态人设适配性差的问题

  - 长周期用户偏好演化的更新逻辑可借鉴三级门控策略：按属性稳定性设置不同更新阈值（如核心偏好需多周期证据，临时偏好单次触发即可），减少偏好突变的错误更新

  - 多范式适配思路可复用：高流量场景用profile-to-LoRA参数化注入状态节省token，低流量/要求高准确率场景直接把状态序列化进prompt，平衡成本与效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长周期角色扮演场景（如AI陪伴、游戏NPC、长期交互智能体）要求角色在叙事演进中保持辨识度，现有方案多使用静态人设，无法实现局部属性更新且不破坏稳定特质，评测也只聚焦固定人设保留、记忆召回，不验证输出是否匹配当前演化后的状态，易出现「状态过时失效」（如早期怕承诺的角色后期结婚后仍输出相关梗）。

### 方法关键点
- 四层状态结构：不可变身份根（姓名、性别、固定背景）+三层可变状态：高阻力persona层（长期性格、说话风格、职业等，慢更）、中阻力session层（单会话内新获取信息、态度转变等）、低阻力moment层（瞬时情绪、触发场景，每场景刷新）
- 跨周期三级门控更新：每个可更新字段设置阻力等级，需同时满足证据覆盖周期数、高显著性事件数量、距上次更新冷却时间三个阈值才允许更新，避免属性频繁波动
- 双范式条件注入：显式文本注入（把树序列化进prompt，效果好）、隐式参数适配（通过超网络把状态映射为LoRA权重，省token）
- 配套评测基准LongEvoRoleBench：统一8个对话数据集（4个长对话测跨周期演化、4个短对话测单场景状态追踪）的下一utterance评测协议，使用角色当前状态而非固定人设做评判

### 关键结果
以Qwen2.5-7B为骨干，对比RAG、PAG、静态人设prompt、各类LoRA适配方案：显式注入范式下，长对话场景比最强文本基线Char、Sem、Emb指标分别提升19.7%、12.4%、15.1%，12个长对话数据集-指标对全部排名第一；隐式范式下省掉所有人设相关token，18个数据集-指标对排名前二。

### 核心结论
长周期交互智能体的状态建模核心是把不变属性、慢变属性、快变属性解耦，用差异化更新规则控制演化节奏，比全量更新或固定人设效果好得多。
