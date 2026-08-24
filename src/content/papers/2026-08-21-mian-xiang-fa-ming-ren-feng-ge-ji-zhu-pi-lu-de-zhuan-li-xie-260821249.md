---
title: Benchmarking Patent Drafting from Inventor-Style Disclosures
title_zh: 面向发明人风格技术披露的专利撰写基准测试与多Agent框架
authors:
- Lekang Jiang
- Wenjun Sun
- Stephan Goetz
affiliations:
- University of Cambridge
- National Science Library, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2608.21249'
url: https://arxiv.org/abs/2608.21249
pdf_url: https://arxiv.org/pdf/2608.21249
published: '2026-08-21'
collected: '2026-08-24'
category: MultiAgent
direction: 多Agent 敏感领域长文本合规生成
tags:
- Multi-Agent Framework
- Long-Text Generation
- LLM Benchmark
- Domain Adaptation
- Privacy-Preserving
one_liner: 构建真实场景披露转专利数据集Dis2Pat，提出可本地部署的多Agent专利撰写框架性能媲美闭源模型
practical_value: '- 敏感业务场景（如用户隐私相关文案生成、内部商品卖点/专利撰写）可复用该本地部署多Agent架构，拆分管理、生成、校验三类角色适配复杂合规生成任务，避免调用外部API泄露数据

  - 长文本生成任务可参考其任务拆分逻辑：先由Manager Agent做信息结构化与子任务路由，再用领域微调的专用生成Agent输出各模块内容，最后由Polisher
  Agent做全局一致性校验与风格统一，效果显著优于单模型端到端生成

  - 缺少真实训练/测试数据时，可复用「用LLM对现有公开数据做去风格化改写生成伪样本」的思路，控制改写规则保留核心信息、移除场景特定格式，低成本构造符合真实业务流程的数据集'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有专利撰写LLM方案大多基于后期结构化、法律化的输入，和真实工作流从发明人提交的非正式、去法律化、带附图的技术披露生成完整专利的核心场景不匹配；同时专利数据高度敏感，无法调用外部闭源API，缺乏对应基准数据集和本地部署的高性能方案。

### 方法关键点
- 数据集：构造Dis2Pat数据集，从已授权专利通过LLM改写生成9.4K条符合发明人风格的伪披露样本，移除专利法律术语和结构，保留核心技术信息，带对应附图，拆分训练集8490条、测试集943条。
- 框架：提出Patent-MAF多Agent框架，全链路基于开源模型本地部署，分为三类角色：Manager Agent对披露信息做结构化，拆分出权利要求、说明书专属的起草材料路由给对应生成Agent；两个专用Drafter Agent分别生成权利要求（LoRA微调开源模型适配法律规范）、说明书（多模态模型处理附图）；Polisher Agent做全局术语统一、一致性校验、风格规范，不新增技术内容。

### 关键实验结果
对比Qwen3-72B、Llama3.3-70B、GPT-5等开源/闭源模型，Patent-MAF的说明书生成整体质量得分85.4，超过GPT-5的85.1；权利要求生成整体质量得分86.7，为所有开源方案最高，语义相似度BERTScore 88.3超过GPT-5的83.8。消融实验显示，移除Manager、Polisher、权利要求微调、附图输入分别带来1-6.6分的效果下降，各模块收益明确。

最值得记住的结论：对于高合规要求、高隐私性的专业领域长文本生成任务，合理的多Agent角色拆分配合小范围领域微调，可以让开源模型达到甚至超过闭源大模型的效果。
