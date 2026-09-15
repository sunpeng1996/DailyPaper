---
title: 'ClinAgent: A ReAct-Based Agent for Conversational Access to Clinical Trial
  Information'
title_zh: ClinAgent：基于ReAct的临床试验信息对话访问智能体
authors:
- Antonino Vaccarella
- Riccardo Cantini
- Domenico Talia
- Paolo Trunfio
- Marianna Talia
- Rosamaria Lappano
- Marcello Maggiolini
affiliations:
- University of Pisa
- University of Calabria
- National Research Council (Italy, Pisa)
- University "Magna Græcia" of Catanzaro
arxiv_id: '2609.13860'
url: https://arxiv.org/abs/2609.13860
pdf_url: https://arxiv.org/pdf/2609.13860
published: '2026-09-12'
collected: '2026-09-15'
category: Agent
direction: Agent · ReAct 垂直领域工具调用RAG
tags:
- ReAct
- RAG
- LLM Agent
- Tool Calling
- Vertical Domain
one_liner: 提出基于ReAct的Agentic RAG系统，支持多轮自然语言跨源查询临床试验信息
practical_value: '- 垂直领域查询类Agent可直接复用ReAct+多工具分层架构：将本地结构化缓存、公开域检索接口、数值分析工具三类能力封装为可调用组件，兼顾数据新鲜度与查询响应效率，适配电商商品/订单/库存查询、广告投放效果查询等场景

  - 大模型选型可参考差异化能力匹配场景：路径规划类任务优先选择带思维链/思考模式的LLM提升决策准确率，端到端响应任务选择综合性能更优的轻量化模型降低推理成本

  - 垂直场景Agent评估框架可直接迁移：从操作有效性、规划质量、工具调用效率、业务方定性评估四个维度构建评估体系，避免单一量化指标无法覆盖业务体验的问题'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有临床试验注册库查询为纯人工流程，需处理海量半结构化数据，缺乏自然语言交互与跨源信息合成能力，操作效率低、出错率高。
### 方法关键点
1. 构建基于ReAct范式的Agentic RAG系统ClinAgent，支持多轮自然语言交互，返回有依据的最新信息；
2. 封装三类工具供Agent动态调用：ClinicalTrials.gov搜索接口、PubMed检索模块、本地缓存临床试验结构化数据集的Python分析器；
3. 采用三阶段评估框架，覆盖操作有效性、规划质量、工具使用效率、专家定性判断四个维度，对比3款LLM后端效果。
### 关键结果
DeepSeek V3.2思考版规划质量表现最优，Gemini 3.0 Flash获得最高整体性能与最强专家评分，验证了Agentic AI提升垂直领域信息获取效率的价值。
