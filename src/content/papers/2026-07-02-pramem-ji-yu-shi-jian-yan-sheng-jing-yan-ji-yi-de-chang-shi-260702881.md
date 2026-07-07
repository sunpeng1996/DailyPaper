---
title: 'PraMem: Practice-derived Experiential Memory for Long-horizon Behavior Prediction'
title_zh: PraMem：基于实践衍生经验记忆的长时序用户行为预测框架
authors:
- Zhuoqun Li
- Boxi Cao
- Jiawei Chen
- Hanshu Zhou
- Ruoxi Xu
- Guiping Jiang
- Ruotong Pan
- Tingting Gao
- Han Li
- Xiangyu Wu
affiliations:
- 中国科学院软件研究所
- 中国科学院大学
- 复旦大学
- Kuaishou Technology
arxiv_id: '2607.02881'
url: https://arxiv.org/abs/2607.02881
pdf_url: https://arxiv.org/pdf/2607.02881
published: '2026-07-02'
collected: '2026-07-07'
category: RecSys
direction: 推荐系统 · LLM长序列行为预测
tags:
- Long-sequence Prediction
- Experiential Memory
- User Profiling
- LLM4Rec
- Memory Management
one_liner: 通过长历史序列预实践构建双模块经验记忆，大幅提升LLM长时序用户行为预测准确率
practical_value: '- 用户画像构建可复用双经验架构：除沉淀用户行为模式（偏好、消费习惯等）外，新增偏置提醒经验库，标注LLM对该类用户易犯的认知错误（如近因效应、刻板印象），预测时直接拼接输入即可降低LLM原生偏差影响

  - 经验更新可借鉴共识校验机制：从用户历史序列采样带标注实践样本迭代试错，仅采纳多轮验证一致的经验更新规则，避免偶发行为干扰画像稳定性，同时经验长度会自发收敛，不会无限制膨胀

  - 可直接复用自我审查机制过滤无效经验：通过扰动历史序列检查经验groundedness，通过生成虚拟场景检查经验泛化性，过滤掉幻觉生成、仅适配单样本的无效经验，保障经验质量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM长时序行为预测存在两个核心痛点：一是分散在超长序列中的用户潜在行为模式难以精准挖掘，二是LLM自带的认知偏差（如近因效应、训练带来的刻板印象）会进一步降低预测准确率；之前的内存压缩范式仅把长序列当负担处理，没有从根本上解决上述问题。

### 方法关键点
- 提出预实践范式，将长历史序列从负担转为训练资源，通过迭代试错构建用户专属双模块经验记忆：Pattern Experience沉淀用户行为模式，Bias-alert Experience提醒LLM针对该用户易犯的认知偏差
- 迭代流程分三步：①经验试错：采样历史片段构造带标注实践样本，用当前经验指导预测暴露不足；②反思提案生成：对比预测与标签生成经验修改提案，通过自我审查机制（扰动序列验真实性、生成虚拟场景验泛化性）过滤无效提案；③共识驱动调整：每T轮从提案池选择多轮一致支持的操作更新经验，避免偶发行为干扰
- 预测时仅需传入短期近邻序列+经验记忆，无需全量长序列输入

### 关键结果
在OmniBehavior（快手多场景行为数据集）、MovieLens-1M两个数据集上对比Truncation、RAG、Mem0、MemOS、ProEx等基线，采用GPT-OSS-120B、Qwen3.5-35B两个backbone验证：①OmniBehavior上PraMem相比最优基线ProEx，ACC从77.7提升到84.7，F1从26.9提升到31.6；②经验记忆可跨LLM迁移，换用Qwen3.5-35B时仍比基线提升7~8个ACC点；③经验长度在60轮后收敛，不会带来额外长上下文负担。

**最值得记住的一句话**：长历史序列不是负担，通过预实践转化为结构化经验同时兼顾用户行为规律与LLM自身缺陷，是破解长时序行为预测难题的新方向。
