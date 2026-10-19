---
title: 'MuninAI: A Self-Hosted Agentic Framework for Independent Research Groups'
title_zh: MuninAI：面向独立研究团队的自托管Agent框架
authors:
- Markus Fischer
- Jens Meiler
- Matthias Elgeti
affiliations:
- Leipzig University Medical School
- Leipzig University
- ScaDS.AI Dresden/Leipzig
- SECAI Dresden/Leipzig
arxiv_id: '2610.23480'
url: https://arxiv.org/abs/2610.23480
pdf_url: https://arxiv.org/pdf/2610.23480
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: 自托管Agent 私有知识库落地
tags:
- SelfHostedAgent
- RAG
- AgentFramework
- Evaluation
- CorpusGrounding
one_liner: 开源自托管科研Agent框架，适配多开源基座，带无标注评估套件，准确率较裸模提升125%
practical_value: '- 可复用自托管Agent的反向SSH隧道架构：企业内部私有知识库（如电商运营规则、用户隐私数据）部署时，通过后端主动发起隧道对外提供服务，无需暴露内网端口，从架构层面规避数据泄露风险

  - 多源异构检索的分槽位排序策略：电商/推荐场景混合站内商品、站外舆情、内部规则等不同可信度数据源时，可按信源优先级分配固定检索槽位，避免低质量内容挤占高可信结果，比全局统一打分更适配业务规则

  - 无人工标注的拒答能力评估方法：将问题对应语料是否存在于知识库作为ground truth，直接复用做内部RAG/Agent系统的拒答能力测试，大幅降低标注成本

  - 生产级Agent的硬编码约束思路：工具调用次数上限、引用标识符校验、执行沙箱隔离等约束用代码实现，比纯prompt引导的稳定性高30%以上，适合高可用生产环境落地'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
科研团队积累的私有文献、未发表成果等数据无法上传公有LLM服务（存在外泄风险），而现有自托管LLM部署普遍缺乏适配私有领域语料的Agent能力，朴素top-k RAG效果甚至低于无检索的裸模型，同时没有可在私有语料上复现的标准化评估体系，落地难度极高。

### 方法关键点
- 架构前后端完全解耦，后端（Agent、知识库、推理服务）全部运行在机构内部，通过反向SSH隧道对外提供服务，无任何inbound端口暴露，从架构层面保障私有数据安全
- 自研Agent harness，集成45个专用工具+4个功能子Agent（全文阅读、多源检索、沙箱代码执行、深度调研），采用迭代式检索+全文阅读逻辑，要求所有回答必须引用原文对应语句否则触发拒答
- 多源检索按信源可信度分配固定槽位，外部检索结果需单独设置相关性阈值，避免低可信度内容挤占高信源结果
- 配套无需人工标注的评估套件，支持删除问题对应语料测试系统拒答率，可复现任意模型、编码器、语料配置下的效果指标

### 关键实验
在199条LitQA2领域问答对上测试，对比裸模型、朴素top5 RAG基线：harness将基础模型准确率从0.387提升至0.874，提升幅度达125%；朴素RAG准确率全部低于裸模型；当问题对应语料从库中移除时，Qwen系列模型90%、gpt-oss-20b 80%的问题会主动拒答，300次伪造引用测试无幻觉。

### 核心结论
对于领域私有知识库的Agent系统，适配场景的harness设计比基座模型本身对效果的影响更大
