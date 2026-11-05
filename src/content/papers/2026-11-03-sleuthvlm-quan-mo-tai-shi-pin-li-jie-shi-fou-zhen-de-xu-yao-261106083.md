---
title: 'SleuthVLM: Do We Really Need Audio-in-Video for Omni Video Understanding?'
title_zh: SleuthVLM：全模态视频理解是否真的需要直接输入音频？
authors:
- Peiran Wu
- Fangfei Gou
- Zhaoxi Mu
- Changhao Zhang
- Jian Liu
- Weiqiang Wang
- Yuntao Wang
- Yuanchun Shi
- Junxiao Shen
affiliations:
- University of Bristol
- Ant Group
- Tsinghua University
arxiv_id: '2611.06083'
url: https://arxiv.org/abs/2611.06083
pdf_url: https://arxiv.org/pdf/2611.06083
published: '2026-11-03'
collected: '2026-11-05'
category: Agent
direction: Agent 全模态视频理解架构优化
tags:
- VLM
- Agent
- Video Understanding
- ASR
- Omni-modal
one_liner: 基于VLM+带时间戳ASR的Agent框架，无需直接音频输入实现SOTA全模态视频理解
practical_value: '- 多模态理解任务可拆分为专用小模型+Agent调度模式，无需盲目投入端到端全模态大模型训练：例如电商商品视频/直播内容理解，可复用成熟ASR转译语音、VLM理解画面，Agent按需调用工具，成本远低于全模态预训练，效果更可控

  - 带时间戳的语义索引可大幅降低长序列处理成本：电商长直播、用户行为视频回溯等场景，可先将音频转成带时间戳的文本作为索引，快速定位相关视频片段，避免全量抽帧处理，算力成本可降低70%以上

  - 业务侧优先复用强推理能力的通用VLM/LLM做Agent调度，ROI高于投入资源做多模态对齐训练：实验证明普通VLM加Agent机制的性能超过同规模经过全模态对齐训练的模型，无需额外预训练即可快速落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有全模态视频理解模型依赖端到端音视频模态对齐训练，需要消耗大量标注配对数据，还会损失原有LLM/VLM的推理和工具调用能力；同时单轮固定采样的处理方式容易漏过长视频中的关键片段，长视频理解性能瓶颈明显。
### 方法关键点
- 音频预处理：单次将视频语音通过ASR转成带词级别时间戳的文本，同时保留无语音的时间间隙，全程不输入原始音频
- Agent沙箱设计：给VLM提供隔离运行环境，开放视频帧提取、裁剪、ASR文本搜索、片段查看等通用工具，仅定义资源调用预算，由VLM自主决策证据收集路径，无需预定义工作流
- 时间索引机制：VLM以带时间戳的ASR文本为索引，快速定位问题相关的视频片段，从粗到细按需抽帧，大幅减少无效计算
### 关键结果
在4个覆盖30秒到90分钟的全模态视频基准测试集上，SleuthVLM（Opus 5.5版本）平均准确率75.0%，超过Gemini 3.8 Flash 2.6个点；登顶Video-MME-v2榜单，准确率77.8%，超过Gemini 3.8 Flash 6.8个点；基于开源27B VLM的版本，性能超过所有开源全模态模型13.8个点。
### 最值得记住的一句话
全模态视频理解的瓶颈是Agent能力，不是直接音频输入，也不是更多模态对齐训练数据。
