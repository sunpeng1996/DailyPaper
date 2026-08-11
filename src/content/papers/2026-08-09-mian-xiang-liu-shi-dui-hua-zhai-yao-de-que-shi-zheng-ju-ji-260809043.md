---
title: 'Don''t Scroll Back: Missing-Evidence Memory for Streaming Dialogue Summarization'
title_zh: 面向流式对话摘要的缺失证据记忆框架ReMEMBER
authors:
- Hyangsuk Min
- Hwanjun Song
affiliations:
- KAIST
arxiv_id: '2608.09043'
url: https://arxiv.org/abs/2608.09043
pdf_url: https://arxiv.org/pdf/2608.09043
published: '2026-08-09'
collected: '2026-08-11'
category: LLM
direction: LLM长上下文 · 对话记忆优化
tags:
- Streaming Summarization
- Long-Context LLM
- Memory Retrieval
- Gap Detection
- Dialogue System
one_liner: 针对流式对话当前窗口的上下文依赖缺口，提出缺口感知的记忆检索精炼框架，提升长历史下摘要质量
practical_value: '- 电商客服Agent的长会话摘要可复用缺口检测逻辑，先识别当前会话窗口的指代/属性/关系缺失，定向召回历史会话证据，避免无关内容占用token预算

  - 长对话RAG系统可借鉴chunk转utterance级精炼trick，从召回的粗粒度块中提取最小有效证据单元，提升固定记忆预算下的证据密度

  - 流式推荐的用户长兴趣建模可参考轮询式证据分配策略，避免单类兴趣占用全部记忆槽，覆盖多维度的兴趣依赖缺口'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有对话摘要大多基于闭域全量对话假设，流式场景下用户仅需要最近会话窗口的自包含摘要，但当前窗口普遍存在指代不明、实体属性缺失、因果关系未说明等上下文缺口。全量历史输入计算成本高且存在长上下文迷失、幻觉等问题，增量/层级摘要方法会丢失细粒度证据，常规检索仅匹配窗口字面相似内容，无法召回缺口所需的隐含依赖证据，无法满足固定预算下的流式摘要需求。
### 方法关键点
- 缺口条件检索：先检测当前窗口中需要摘要且存在上下文缺口的单轮对话，针对每个缺口生成证据查询，联合BM25稀疏检索与语义稠密检索，用倒数秩融合得到候选chunk
- 缺口条件chunk精炼：将每个候选chunk拆解为单轮utterance，基于与缺口查询的语义相似度重排，提取高相关的单轮证据单元，过滤冗余内容
- 缺口平衡证据积累：采用轮询式分配策略，从每个缺口的候选证据中按轮次取最高得分单元，直到触达记忆token预算，避免单个缺口占用全部记忆空间
### 关键实验
在覆盖闲聊、办公场景、历史长度7K-160K token的900个对话样本上测试，固定1024 token记忆预算下，ReMEMBER的记忆召回率达0.6984，比最优混合检索基线高15.7个百分点；缺口解析完整度最高提升17个百分点，记忆构建延迟稳定在4s左右，不受历史长度增长影响。
### 核心结论
流式长上下文任务的核心瓶颈不是历史访问量，而是记忆能否准确恢复当前窗口预设的依赖证据，而非仅匹配字面相似内容。
