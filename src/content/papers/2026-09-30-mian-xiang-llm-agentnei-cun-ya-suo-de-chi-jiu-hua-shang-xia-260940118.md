---
title: Persistent Context Graphs for Efficient Memory Compaction in LLM Agents
title_zh: 面向LLM Agent内存压缩的持久化上下文图方法RECAP
authors:
- Jingbo Yang
- Kwei-Herng Lai
- Xiaowen Wang
- Zhaoxuan Tan
- Pei Zhou
- Mengting Wan
- Yaar Harari
- Evgeniy Gabrilovich
- Shiyu Chang
affiliations:
- University of California, Santa Barbara
- Microsoft
- University of Notre Dame
arxiv_id: '2609.40118'
url: https://arxiv.org/abs/2609.40118
pdf_url: https://arxiv.org/pdf/2609.40118
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: Agent 内存优化·上下文管理
tags:
- LLM Agent
- Memory Compaction
- KV Cache
- Attention
- Context Management
one_liner: 复用LLM推理原生注意力构建持久化上下文图，零额外模型调用实现Agent内存高效压缩
practical_value: '- 电商智能客服、导购Agent等多轮会话场景可复用推理原生注意力做历史重要性打分，无需额外调用LLM做摘要压缩，大幅降低上下文管理开销

  - 会话式推荐的上下文选择可复用「历史重要性+当前query IDF加权关键词匹配+依赖边回溯」逻辑，既能适配当前需求，还可恢复之前丢弃的关键历史块，避免信息丢失

  - 用户间隔长、KV cache易失效的场景（如电商咨询、低频会话推荐）可用轻量持久化图（单会话仅占几十KB内存）快速筛选上下文，相比摘要式压缩降低95%左右冷启动延迟

  - 调用黑盒LLM无法获取注意力时，可用同系列小模型重放会话计算注意力作为替代，效果几乎无损失，大幅降低适配成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长周期LLM Agent的会话历史易超出上下文窗口，现有压缩方案要么依赖额外LLM调用做摘要，推高计算成本；要么KV cache压缩策略在缓存因用户长时间闲置失效后，需要重编码全量历史，且无法适配后续query转向导致的历史信息需求变化，压缩后信息丢失不可逆。

### 方法关键点
- 构建持久化上下文图：节点为会话原子块（用户消息、工具调用+结果、助理消息），存储注意力EMA累加的重要性得分，边为块间注意力依赖（超过阈值则建边），完全复用推理原生注意力计算，无额外开销
- Query驱动上下文选择：结合历史重要性+当前query与历史块的IDF加权关键词匹配得分排序，优先保留保护块（所有用户消息、每个文件最新修改记录），按预算填充高得分块后回溯1-hop依赖边补充支撑上下文，全程仅做图遍历和字符串匹配，无模型调用
- 兼容prefix缓存：缓存有效时直接复用，仅缓存失效时触发图筛选，图更新在CPU后台执行不占关键路径

### 关键结果
在SWE-Together、Lost-in-Conversation代码任务上对比全量历史、摘要式压缩、KV eviction、LLMLingua等基线：
1. 相比Codex默认摘要压缩，RECAP将压缩+冷恢复延迟降低约95%
2. Lost-in-Conversation准确率比全量历史分别高19.8、41.2个百分点
3. SWE-Together任务保持效果相当的前提下，历史上下文长度减半，单会话上下文图仅占用几KB到十几KB CPU内存

**最值得记住的一句话：** LLM推理过程中本就会计算的注意力是免费且高效的会话历史重要性信号，用持久化图存储这类原生信号可以大幅降低Agent上下文管理的开销
