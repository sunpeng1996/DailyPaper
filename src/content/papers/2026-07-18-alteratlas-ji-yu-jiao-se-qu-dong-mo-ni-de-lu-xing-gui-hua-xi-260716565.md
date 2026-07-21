---
title: 'AlterAtlas: Shifting Travel Planning from AI Generation to Validation via
  Persona-Driven Simulations'
title_zh: AlterAtlas：基于角色驱动模拟的旅行规划生成转校验系统
authors:
- William Huang
- Ruofei Du
- Yang Zhang
affiliations:
- University of California, Los Angeles
- Google
arxiv_id: '2607.16565'
url: https://arxiv.org/abs/2607.16565
pdf_url: https://arxiv.org/pdf/2607.16565
published: '2026-07-18'
collected: '2026-07-21'
category: Agent
direction: Agent 角色模拟 · 旅行规划校验
tags:
- Persona Agent
- Simulation
- Travel Planning
- Human-AI Interaction
- LLM Agent
one_liner: 提出基于用户角色与地理空间数据的旅行模拟校验框架，替代传统单次生成式规划流程
practical_value: '- 多角色场景的推荐/规划可复用「生成候选→Persona模拟校验→迭代修正」范式，替代单次生成，比如电商多人拼单/家庭场景商品推荐、多人出行行程推荐，先跑模拟识别需求冲突再优化，分辨率远高于直接生成

  - 可复用显式用户状态变量设计，把用户隐性约束（如疲劳、预算敏感度、忌口）拆解为可量化、可更新的Simulation Variables，每个变量定义更新规则与依赖，解决LLM生成时对隐性约束漏判的问题

  - 偏好 elicitation 可借鉴案例驱动思路，无需直接询问用户偏好，先输出候选方案的模拟结果，引导用户通过反馈修正偏好/角色画像，比空泛的偏好调研转化率更高，适合电商/本地生活冷启动用户建模

  - 工程上可复用「工具链绑定+DSPy小样本优化+结构化输出校验」的Agent实现范式，POI/商品召回绑定垂直领域工具，输出用Pydantic做schema校验，大幅降低幻觉对下游逻辑的影响'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM旅行规划工具均采用单次生成成品方案的交互范式，未考虑用户动态约束（如疲劳、过敏、同行人需求冲突）与方案潜在失败点，也不匹配用户天然的迭代规划习惯，用户需手动校验可行性，对生成方案的信任度低。

### 方法关键点
- 四层核心工作流：用户先定义可编辑出行Persona与对应模拟变量（如疲劳、饥饿、过敏程度，自带更新规则与依赖项）→ 绑定Google Places、web搜索工具做POI召回，由用户标记「必去」「想去」优先级 → 生成候选行程，强制保留必去POI，灵活调整可选点位 → 逐节点模拟每个角色的行程体验，输出实时状态、感知反馈与优化建议，支持迭代修正行程或Persona参数。
- 技术实现：核心推理采用Gemini 3.0 Flash，POI/行程生成模块基于PydanticAI开发，模拟/优化建议模块用DSPy做小样本优化，所有输出用Pydantic做结构化校验，降低幻觉。

### 关键结果
- 专家评估51对「初始生成/模拟修正」行程，修正后行程与Persona偏好的对齐度评分平均提升0.49（p<0.01），可行性评分基本稳定（初始8.1/10，修正后8.2/10）。
- 11人内组用户研究显示，相比用户自有AI规划流程，AlterAtlas在计划理解度、约束识别率、最终方案信心度上均显著提升，4名实际使用行程出行的用户反馈模拟的疲劳/约束预判准确率高，可有效规避行程问题。

### 核心结论
AI规划不应作为终点，而应作为迭代校验的起点，用可解释的模拟把用户的隐性心智过程外显化。
