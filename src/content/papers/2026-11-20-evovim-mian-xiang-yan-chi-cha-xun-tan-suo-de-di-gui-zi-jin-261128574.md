---
title: 'EvoViM: Recursively Self-Evolving Visual Agents for Exploration with Deferred
  Queries'
title_zh: EvoViM：面向延迟查询探索的递归自进化视觉Agent框架
authors:
- Xinyu Cao
- Tianjie Ju
- Zhuosheng Zhang
affiliations:
- Shanghai Jiao Tong University
- Hunan University
- National University of Singapore
arxiv_id: '2611.28574'
url: https://arxiv.org/abs/2611.28574
pdf_url: https://arxiv.org/pdf/2611.28574
published: '2026-11-20'
collected: '2026-11-25'
category: Agent
direction: 多模态Agent · 自进化视觉记忆
tags:
- Multimodal Agent
- Self-Evolution
- Visual Memory
- Deferred Query
- MLLM
one_liner: 基于冻结MLLM递归进化视觉程序，解决延迟查询场景下的视觉证据留存与使用问题
practical_value: '- 做电商多模态Agent（如商品浏览巡检、直播间信息抓取）时，可复用「视觉程序+像素级匹配」的方案替代文本记忆，避免相似商品/图案的识别误差

  - Agent自迭代优化可借鉴该框架的「失败归因→局部程序修订→校验门控」流程，无需微调模型即可通过修改工具、提示词、记忆逻辑提升效果

  - 延迟查询场景（如先逛后搜、浏览历史召回相似商品）可参考「交互先验引导记忆留存规则」设计，避免提前预设的记忆规则遗漏关键信息

  - 工程实现上，可将高频视觉匹配、状态提取逻辑下沉为代码工具，大幅降低MLLM调用的token消耗与延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有MLLM Agent记忆方案存在明显缺陷：人工设计的存储规则适配性差，基于交互进化的文本记忆会丢失难以用文字描述的视觉细节，在延迟查询场景（先探索环境后披露查询需求）下完全无法满足要求，比如先逛线下门店/线上商品池后找特定图案款、先浏览直播间后召回对应商品这类业务场景，现有方案都存在高误差。
### 方法关键点
- 基于冻结MLLM进化统一视觉程序，同时承载记忆留存规则和任务执行技能，直接基于像素处理视觉证据，不依赖文本转译，避免视觉细节丢失
- 迭代流程：MLLM用当前程序执行任务，基于开发集的失败轨迹归因到对应操作漏洞，修订程序的存储逻辑、工具函数、调用提示词，再通过代码校验+效果门控判断是否保留新版本
- 递归进化：修订过程中同步更新指导后续迭代的规则手册、分析脚本，避免重复尝试无效修改，提升迭代效率
### 关键实验
覆盖6类任务（3类延迟查询任务+卡片匹配、俄罗斯方块、吃豆人），测试3款主流MLLM（GPT-6.1 Sol、Claude Haiku 5.5、Qwen3.8-27B），对比AutoMem等6个基线：
- 平均得分比最强基线AutoMem高31.3~47.6个百分点
- 延迟查询任务上，解决了文本记忆无法区分相似视觉元素的问题，准确率比纯文本记忆基线高2~5倍
- 多数任务下进化后的程序token消耗比初始版本更低，推理效率更高
### 核心结论
对于需要留存视觉细节的MLLM Agent任务，无需微调模型，通过自进化视觉程序的方式就能大幅提升效果，表现远优于纯文本记忆或人工设计的视觉存储方案
