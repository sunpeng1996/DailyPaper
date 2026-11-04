---
title: A Circuit for In-Context Learning
title_zh: 上下文学习的内部计算电路机制解析
authors:
- Andrew Gao
- William Gao
affiliations:
- Stanford University
arxiv_id: '2611.05344'
url: https://arxiv.org/abs/2611.05344
pdf_url: https://arxiv.org/pdf/2611.05344
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: LLM 上下文学习内部机制解析
tags:
- In-Context Learning
- Transformer
- Attention Head
- Causal Intervention
- Circuit Analysis
one_liner: 定位3~4B Transformer中ICL全链路功能头，还原从样本存储到输出的完整因果机制
practical_value: '- 构建Agent/生成式推荐的few-shot prompt时，主动加入重复标注触发gate机制，可将小参数模型ICL准确率从20%提升至90%+，避免单样本每类的效果退化

  - 优化LLM4Rec的few-shot效果时，可增加同类demo数量、分散标注写入层，放大reader头的累加增益，降低单头输出不足导致的结果波动

  - 做ICL场景的推理优化时，可裁剪非核心的冗余注意力头计算，仅保留不到200个writer/reader/brake等功能头，即可保留60%以上的ICL性能，降低推理时延'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有上下文学习（ICL）机制研究仅识别了零散的独立功能头，未明确各组件的协同逻辑，无法解释ICL的门控触发、近因偏置抑制等行为，也难以为业务场景的ICL效果优化、推理加速提供可落地的指导。
### 方法关键点
- 针对Qwen3-4B、SmolLM3-3B、Llama-3.2-3B三个3~4B参数基座模型，采用激活补丁、头消融、残差方向steering等因果干预手段，全链路定位ICL的功能组件
- 构建4类孪生prompt测试集，通过最小对变量控制分离标注slot存储、类别匹配、门控、结果输出等各阶段的作用
- 提出ICL的KV内存实现范式：每个标注token作为独立slot，存储对应样本的类别key与标签value，经过门控触发、类别匹配、标签拷贝、近因偏置抑制四个阶段输出结果
### 关键结果
- 共定位7类核心功能头：16个重复检测头、~20个writer头（写类别key到slot）、~90个reader头（匹配query与slot key）、2个query编码头、24个brake头（抑制近因偏置）、~20个copier头（输出logit），以及全局门控信号g
- 移除brake头可让ICL margin提升1.39nats（接近3倍），但会引入严重的近因偏置；单头最大贡献仅0.2nats，1.3nats的分类结果需要至少7个reader头累加
- 当prompt中存在重复标注时gate打开，ICL准确率从单样本每类的20%提升至6样本每类的96%；仅保留不到200个核心功能头即可保留60%以上的ICL性能

ICL本质是Transformer内部由注意力头搭建的门控关联查表系统，全链路计算过程可被完整因果追踪
