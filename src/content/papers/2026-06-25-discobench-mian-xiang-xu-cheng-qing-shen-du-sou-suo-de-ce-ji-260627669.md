---
title: 'When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search'
title_zh: DISCOBENCH：面向需澄清深度搜索的Agent评测基准
authors:
- Yiling Tao
- Shihan Deng
- Meiling Tao
- Pengzhi Wei
- Zhichao Hu
- Zhihao Zhu
affiliations:
- Hunyuan, Tencent
- Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2606.27669'
url: https://arxiv.org/abs/2606.27669
pdf_url: https://arxiv.org/pdf/2606.27669
published: '2026-06-25'
collected: '2026-07-03'
category: Agent
direction: 搜索Agent · 歧义澄清基准
tags:
- Search Agent
- Clarification
- Benchmark
- Multi-turn Interaction
- Deep Search
one_liner: 构建覆盖11领域的歧义交互基准，评估搜索Agent主动识别歧义并发起询问的能力
practical_value: '- 电商导购/复杂搜索Agent可复用4种歧义分类（实体/版本/评判标准/事实错误）设计主动询问触发逻辑，减少多步推理的级联错误

  - 多步搜索场景下，检测到歧义时优先询问的节点通过率达93.4%，远高于反复搜索的51.9%，可直接调整策略优先级，避免无意义的搜索资源消耗

  - 构建内部Agent交互评测集时，可参考其「半自动化向多步推理链注入歧义+LLM用户模拟器提供线索」的流程，大幅降低人工标注成本

  - 现有搜索Agent可快速落地优化：在prompt中明确提示主动检测歧义，平均能提升5%左右的端到端准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM驱动的深度搜索Agent默认用户初始query完整明确，但真实场景中用户常因记忆模糊、认知限制给出模糊/歧义query，多步推理下歧义会级联传播导致全路径错误，浪费计算资源。现有检索基准大多假设query无歧义，歧义相关数据集多为静态场景，缺乏覆盖多步搜索动态歧义交互的评测体系。

### 方法关键点
- 构建DISCOBENCH基准，包含211个多步搜索样本、463个歧义实例，覆盖11个真实领域、4类歧义（实体/版本/评判标准/事实错误），按歧义点数量分为易/中/难三个难度等级
- 设计分层评估框架：搭建LLM用户模拟器渐进式放出区分线索，从任务效用、歧义检测、交互策略、成本效率4个维度综合评估Agent能力
- 设置两种评测模式：Neutral模式无歧义相关提示，测Agent主动检测交互的原生能力；Guided模式明确提示注意歧义，测模型能力上限

### 关键实验
在11款主流闭源LLM上完成评测：Neutral设置下最优模型Doubao-Seed-2.0-Pro端到端准确率仅43.1%；Guided设置下所有模型平均端到端准确率从28.6%提升至33.7%，歧义检测F1从45.3%提升至64.9%；检测到歧义后先搜索再询问的节点通过率达93.4%，远高于直接猜测的56.5%、反复搜索再猜测的51.9%。

### 核心结论
反复搜索不澄清的表现比直接猜测还差，搜索Agent的核心优化方向不是增加搜索次数，而是在正确的歧义节点主动发起交互。
