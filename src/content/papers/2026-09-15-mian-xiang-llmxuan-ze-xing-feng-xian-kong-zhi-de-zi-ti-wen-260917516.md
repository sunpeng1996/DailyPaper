---
title: When Should LLMs Abstain? Chain-of-Self-Questioning for Selective Risk Control
title_zh: 面向LLM选择性风险控制的自提问链（CoSQ）应答决策框架
authors:
- Ali Şenol
affiliations:
- Tarsus University, Türkiye
arxiv_id: '2609.17516'
url: https://arxiv.org/abs/2609.17516
pdf_url: https://arxiv.org/pdf/2609.17516
published: '2026-09-15'
collected: '2026-09-16'
category: LLM
direction: LLM风险控制 · 选择性应答幻觉抑制
tags:
- Hallucination-Mitigation
- Selective-Prediction
- Prompt-Engineering
- Risk-Control
- Chain-of-Thought
one_liner: 纯提示式自提问链框架，无需微调即可让LLM自主判断应答或拒答，降低幻觉风险
practical_value: '- 高风险业务场景（电商客服应答、营销文案生成、Agent工具调用决策）可直接复用CoSQ三阶段提示框架：先分解应答所需信息单元→逐个评估置信度→达标才输出结果，无需微调即可降低幻觉，避免错误回复带来的客诉/资损

  - 可根据业务成本灵活调参：错误容忍度极低的场景（金融类商品导购、售后政策解答）用τ=0.90的Grounded-CoSQ；需要更高覆盖率的通用咨询场景用Critical-CoSQ，仅校验核心信息置信度，兼顾覆盖和准确率

  - 可与RAG系统搭配落地：检索到外部文档后先调用CoSQ校验信息匹配度、可信度，再决定是否生成应答，比事后校验节省无效回答带来的后续处理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM在事实支撑不足时仍会生成流畅的幻觉回复，传统CoT、RAG等方法未在生成前做应答/拒绝的决策，高风险场景下错误回复的代价远高于转人工/拒绝回答；现有选择性回答方法大多需要微调或多模型协作，无法适配黑盒/托管LLM场景。

### 方法关键点
- 纯提示三阶段框架，无需微调、无需访问模型logits，适配所有通用LLM：1）分解回答问题所需的所有信息单元；2）逐个评估每个信息单元的置信度；3）根据预设阈值判断是否输出应答，否则返回拒答
- 三种可按需选择的变体：Grounded-CoSQ取所有信息单元平均置信度过阈值，均衡性最优；Critical-CoSQ仅校验核心信息置信度，覆盖率更高；Adaptive-CoSQ同时校验三类置信度条件，风险最低

### 关键实验
在817题的TruthfulQA多选择验证集上测试11个开源/托管LLM，对比CoT基线，τ=0.90的Grounded-CoSQ将无条件错误应答率从13.1%降至8.9%，相对下降32.1%，应答准确率从86.9%提升至89.7%，应答覆盖率87.6%，所有模型均稳定获益；在300题的Natural Questions短答数据集上也验证了泛化性，错误应答率相对下降33.5%。

### 核心结论
可靠的LLM系统不仅要衡量输出答案的准确率，还要明确模型在什么情况下应该选择不回答，根据业务的错误成本和覆盖要求选择合适的风险-覆盖率平衡点。
