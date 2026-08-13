---
title: 'AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses'
title_zh: 测试阶段强到弱能力迁移：基于推理Harness的无参数更新能力传递
authors:
- Cheng Qian
- Wenting Zhao
- Liangwei Yang
- Heng Wang
- Jielin Qiu
- Heng Ji
- Silvio Savarese
- Huan Wang
- Shelby Heinecke
affiliations:
- Salesforce AI Research
- University of Illinois Urbana-Champaign
arxiv_id: '2608.12307'
url: https://arxiv.org/abs/2608.12307
pdf_url: https://arxiv.org/pdf/2608.12307
published: '2026-08-11'
collected: '2026-08-13'
category: Agent
direction: Agent Harness · 无微调跨模型能力迁移
tags:
- Agent_Harness
- Capability_Transfer
- Test_Time_Adaptation
- LLM_Scaffolding
- Inference_Optimization
one_liner: 强模型仅用5%验证集生成推理Harness，无需微调弱模型就将其ToM任务准确率从0.49提升至0.91
practical_value: '- 小模型业务落地可跳过蒸馏微调，直接用强模型为垂类小模型生成任务特定Harness（格式校验、路由、确定性规则），成本低上线快，可复用在电商客服、推荐query理解等场景

  - 优化Harness仅需5%左右的小样本验证集即可获得无明显过拟合的稳定效果，且提升builder模型推理深度的收益远高于增加验证迭代次数，可节省大量算力

  - 针对基线效果已较好的强模型不要过度加Harness，需按子任务headroom（基线与天花板准确率差）选择性加约束，避免干扰模型原有正确推理，适合推荐相关性判分等已成熟的子场景

  - 可落地自动Harness迭代管线：用强元模型基于少量验证数据自动生成、迭代任务推理流程，替代人工编写prompt、规则，大幅降低运营人力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有蒸馏等跨模型能力迁移方案均需更新弱模型参数，训练成本高、上线周期长；实际部署中小模型常嵌入包含prompt、路由、校验的推理管线，但缺乏系统的测试阶段无参数更新能力转移方案。

### 方法关键点
- 分为两阶段流程：第一阶段强builder模型仅能访问5%的带标注验证集，迭代生成包含prompt模板、任务路由、确定性求解器、格式校验、验证回路的可执行Harness；第二阶段用固化的Harness在全量隐藏测试集上测试弱target模型效果，全程不更新弱模型参数
- 控制变量覆盖11种不同能力的builder模型、2种target模型、3种builder运行平台，对比builder推理努力程度、验证迭代次数等变量的影响

### 关键实验结果
- 数据集为4个经典Theory-of-Mind推理基准，共3900条测试样本，验证集仅占5%（195条）；基线为弱模型直接调用、人工设计的UserHarness
- 100%的builder配置均能提升弱模型效果，弱模型GPT-5.4-mini平均准确率从0.49提升至0.76（绝对+0.275），最优配置（GPT-5.5作为builder）准确率达0.91，相对提升86.7%，效果超过未加Harness的更强模型GPT-5.4
- 效果提升主要来自格式强制校验、确定性逻辑卸载、任务路由，而非引导弱模型输出更长推理链；builder推理深度与最终效果单调正相关，平台影响极小，越弱的target模型收益越大

### 核心结论
推理时Harness优化是训练时蒸馏的重要补充，给小模型搭配合适脚手架的收益可能高于直接升级更大的无脚手架模型。
