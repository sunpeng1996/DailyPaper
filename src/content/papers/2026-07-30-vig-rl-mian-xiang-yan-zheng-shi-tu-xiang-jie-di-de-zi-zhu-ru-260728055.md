---
title: 'VIG-RL: Learning to Search and Insert for Verified Image Grounding'
title_zh: VIG-RL：面向验证式图像接地的自主搜索插入学习框架
authors:
- Qinhan Yu
- Jun Guang
- Chong Chen
- Wentao Zhang
affiliations:
- Peking University
- Huawei Cloud BU
arxiv_id: '2607.28055'
url: https://arxiv.org/abs/2607.28055
pdf_url: https://arxiv.org/pdf/2607.28055
published: '2026-07-30'
collected: '2026-07-31'
category: Agent
direction: 多模态Agent · 验证式图像接地
tags:
- VIG
- ReAct
- GRPO
- Multimodal Agent
- RLHF
- RAG
one_liner: 用GRPO强化学习优化ReAct多模态Agent，动态决策检索与图片插入，远超静态RAG基线
practical_value: '- 电商图文混排生成（商品详情页、种草攻略、操作教程）场景可复用符号化图片ID引用方案，全部使用检索到的真实素材，完全规避生成式图片幻觉，提升内容可信度

  - 训练工具调用Agent时可复用复合奖励设计：先加格式合规门控奖励，再拆分文本质量、检索召回、插入精度多维度子奖励，避免纯LLM打分的奖励黑客问题

  - 知识密集场景图像检索优先采用上下文锚定方案（图片与关联文本绑定，检索时比对query和图片关联文本语义相似度），比直接CLIP跨模态检索准确率更高

  - 动态自适应检索优于固定K的静态RAG，可参考多轮搜索逻辑，根据当前信息缺口决定是否再次检索，平衡信息覆盖与上下文噪音'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态生成存在两类核心缺陷：生成式图片易出现事实幻觉，无法满足知识密集场景的真实性要求；静态RAG采用检索-生成解耦的固定流程，无法动态决策何时需要检索、检索什么内容、图片插入到文本的哪个位置，图文匹配度和插入合理性差。电商商品攻略、百科知识回答、操作教程等场景对内容真实性、图文匹配度要求极高，现有方案无法满足需求。

### 方法关键点
- 采用ReAct式交互循环，动作空间包含三类：文本搜索补全上下文、图像搜索获取真实素材、生成最终图文混排回答；检索到的图片映射为唯一符号ID，生成时仅输出ID标识插入位置，渲染时替换为真实图片，完全规避图片幻觉
- 采用GRPO算法做RL优化，复合奖励设计：格式奖励作为门控，轨迹不合规直接得0分；文本质量奖励用LLM评估内容正确性；图片插入精度奖励用规则计算插入图片的precision，避免奖励黑客；搜索过程奖励计算检索候选池的gold图片召回率，鼓励有效检索
- 图像检索采用上下文锚定方案：每张图片和其关联的上下文文本绑定，检索时匹配query与图片关联文本的语义相似度，解决直接跨模态检索的语义偏移问题

### 关键实验结果
在MRAMG-Bench 6个覆盖不同领域的数据集上测试，对比静态RAG、零样本Agent、SFT基线：VIG-RL-8B比同backbone静态RAG的Image F1从57.7提升到78.9（+21.2），综合得分C.S.从56.4提升到78.1（+21.7），跨域数据集也保持SOTA表现；比SFT基线在Arxiv数据集上C.S.提升39.9。

**最值得记住的结论**：动态RL优化的Agent在多模态图文接地任务上，效果显著优于固定流程的静态RAG和纯模仿学习方案。
