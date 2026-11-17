---
title: Sage S2.1 Flash Technical Report
title_zh: Sage S2.1 Flash：320B参数MoE多模态科学智能体技术报告
authors:
- Kun Cai
- Haodong Chen
- Guangran Cheng
- Qingxiu Cheng
- Xu Dai
- Guanting Dong
- Qiming Ge
- Lixin Gu
- Tao Gui
- Honglin Guo
affiliations:
- Shanghai AI Laboratory
- Fudan University
- Institute of Software Chinese Academy of Sciences
- Renmin University of China
- Institute of Automation Chinese Academy of Sciences
arxiv_id: '2611.21072'
url: https://arxiv.org/abs/2611.21072
pdf_url: https://arxiv.org/pdf/2611.21072
published: '2026-11-15'
collected: '2026-11-17'
category: Agent
direction: 科学多模态Agent · MoE大模型
tags:
- MoE
- Multimodal Agent
- Tool Orchestration
- Scientific Reasoning
- LLM
one_liner: 发布320B参数MoE多模态科学智能体，在7大域33个基准上取得领先性能
practical_value: '- 电商多工具编排Agent训练可复用ToolSpace框架：基于真实的客服、导购、运营工具调用轨迹构建工具依赖图，自动合成跨工具长流程任务，配套自动校验脚本，解决长路径Agent训练数据稀缺的问题。

  - 推荐/广告系统的Agent化运维、智能客服场景可借鉴可验证轨迹筛选方案：采用任务执行结果+环境状态变化双校验逻辑筛选SFT轨迹，大幅降低Agent幻觉导致的执行错误。

  - 商品多模态理解、专业内容推荐场景可复用Sage Sci-Perception架构：针对商品参数、工业图纸、专业文档等异构输入，采用分模态编码器+共享投影层的设计，低成本对接通用LLM主干，无需大幅调整预训练模型。

  - 长路径导购Agent训练可采用状态感知随机游走+回滚重采样方法：生成高难度多步骤的训练样本，提升Agent处理复杂用户需求、跨环节完成导购任务的成功率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态Agent在科学场景下普遍存在异构输入处理能力不足、长流程工具编排准确率低、任务执行结果缺乏可校验性的问题，通用Agent缺乏针对性的科学领域感知、推理与交互式执行能力，难以支撑复杂科研工作流落地。
### 方法关键点
- 架构：采用320B参数MoE主干，混合稀疏+线性注意力支持长上下文处理；Sage Sci-Perception模块对接分子、蛋白、光谱等异构科学输入，经分模态专用编码器提取特征后，通过专属投影层映射到主干输入空间，与文本、图像实现统一处理。
- 训练：构建覆盖工具使用、搜索、编码、ML实验、科学软件交互的大规模可验证训练环境；提出ToolSpace框架，基于真实调用轨迹构建工具依赖图，自动合成跨环境长流程任务，配套反绎合成验证脚本，筛选高可靠SFT轨迹；科学模态适配阶段冻结主干与编码器，用GRPO强化学习微调投影层，优化科学证据的表征适配性。
### 关键实验
在7大域33个基准上与DeepSeek-V4.1-Flash、Qwen3.8-Max、GPT-5.6 Sol、Claude Opus 5等5个主流SOTA模型对比，取得OfficeQA Pro（72.2）、MLE-bench Lite（90.3 HumanRank）、Harvey LAB、SpreadsheetBench 2四项第一，OSWorld-Verified（85.2）、WebArena-Verified（67.6）等七项第二，长流程任务表现尤为突出。
### 核心结论
Agent能力的规模化提升核心依赖可验证训练环境的构建，工具是Agent能力的原子单元，基于真实执行轨迹合成的训练数据质量远高于人工构造的伪数据。
